from flask import Flask, request, jsonify, render_template
import json
import os
from ai_module import analyze_with_ai
from fallback import fallback_analysis
from risk_engine import calculate_risk
from utils import is_similar

app = Flask(__name__)

DATA_FILE = "data/incidents.json"


# Helper: Load data
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


#  Helper: Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


#  UI Route
@app.route("/")
def home():
    return render_template("index.html")


# Add Incident (AI + Fallback + Risk + Duplicate Detection)
@app.route("/add", methods=["POST"])
def add_incident():
    data = request.json
    description = data.get("description")

    #  Validation
    if not description or description.strip() == "":
        return jsonify({"error": "Description is required"}), 400

    incidents = load_data()

    # 🔍 Duplicate / Similarity Check
    similar_found = False
    for incident in incidents:
        if is_similar(description, incident["description"]):
            similar_found = True
            break

    # AI analysis
    ai_result = analyze_with_ai(description)

    # Fallback if AI fails
    if not ai_result:
        ai_result = fallback_analysis(description)

    # Risk scoring
    risk = calculate_risk(ai_result, description, incidents)

    new_incident = {
        "id": len(incidents) + 1,
        "description": description,
        "analysis": ai_result,
        "risk": risk,
        "duplicate": similar_found
    }

    incidents.append(new_incident)
    save_data(incidents)

    return jsonify({
        "message": "Incident added",
        "data": new_incident
    })


#  View All Incidents
@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(load_data())


# Search Incidents
@app.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("q", "").lower()
    incidents = load_data()

    filtered = [
        i for i in incidents
        if keyword in i["description"].lower()
    ]

    return jsonify(filtered)
@app.route("/update/<int:id>", methods=["PUT"])
def update_incident(id):
    data = request.json
    incidents = load_data()

    for i in incidents:
        if i["id"] == id:
            i["status"] = data.get("status", "updated")
            save_data(incidents)
            return jsonify({"message": "Updated", "data": i})

    return jsonify({"error": "Not found"}), 404


#  Security Digest
@app.route("/digest", methods=["GET"])
def get_digest():
    incidents = load_data()

    total = len(incidents)
    high = sum(1 for i in incidents if i.get("risk", {}).get("level") == "HIGH")
    medium = sum(1 for i in incidents if i.get("risk", {}).get("level") == "MEDIUM")

    #  Determine top action
    phishing_count = sum(
        1 for i in incidents
        if i.get("analysis", {}).get("type") == "phishing"
    )

    if phishing_count >= 2:
        top_action = "Enable 2FA immediately due to repeated phishing attempts"
    elif high > 0:
        top_action = "Review recent activity and secure sensitive accounts"
    else:
        top_action = "No urgent threats detected. Stay cautious"

    return jsonify({
        "message": "Security Digest",
        "total_incidents": total,
        "high_risk": high,
        "medium_risk": medium,
        "top_action": top_action
    })
if __name__ == "__main__":
    app.run(debug=True)