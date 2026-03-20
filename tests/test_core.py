import requests

BASE_URL = "http://127.0.0.1:5000"

# ✅ Happy Path Test
def test_add_valid():
    res = requests.post(f"{BASE_URL}/add", json={
        "description": "Test OTP scam"
    })
    assert res.status_code == 200


# ⚠️ Edge Case Test
def test_add_empty():
    res = requests.post(f"{BASE_URL}/add", json={
        "description": ""
    })
    assert res.status_code == 400