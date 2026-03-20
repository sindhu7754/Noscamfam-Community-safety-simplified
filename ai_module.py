def analyze_with_ai(text):
    """
    Simulated AI response (acts like LLM for now)
    Now includes explainability for transparency
    """

    text_lower = text.lower()

    # 🔥 Phishing detection
    if "otp" in text_lower or "bank" in text_lower:
        return {
            "type": "phishing",
            "severity": "high",
            "summary": "Possible phishing attempt involving sensitive information",
            "confidence": 0.9,
            "explanation": "Detected keywords like 'OTP' or 'bank' commonly used in phishing attacks",
            "actions": [
                "Do not share OTP",
                "Block the number",
                "Report the message"
            ]
        }

    # 🔐 Credential attack detection
    elif "password" in text_lower:
        return {
            "type": "credential_attack",
            "severity": "medium",
            "summary": "Suspicious attempt to access account credentials",
            "confidence": 0.8,
            "explanation": "Detected keyword 'password' indicating a possible credential theft attempt",
            "actions": [
                "Change password immediately",
                "Enable 2FA"
            ]
        }

    # ⚠️ Unknown → fallback will handle
    else:
        return None