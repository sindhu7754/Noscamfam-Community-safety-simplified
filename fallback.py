def fallback_analysis(text):
    text_lower = text.lower()

   
    if "hate" in text_lower or "angry" in text_lower:
        return {
            "type": "noise",
            "severity": "low",
            "summary": "Non-actionable content filtered",
            "confidence": 0.7,
            "explanation": "Detected emotional or non-informative content",
            "actions": ["Ignored"]
        }

    
    if "otp" in text_lower:
        return {
            "type": "phishing",
            "severity": "high",
            "summary": "OTP-based scam detected (fallback)",
            "confidence": 0.6,
            "explanation": "Fallback rule matched keyword 'OTP'",
            "actions": ["Do not share OTP"]
        }

  
    return {
        "type": "unknown",
        "severity": "low",
        "summary": "Could not classify",
        "confidence": 0.5,
        "explanation": "No known keywords detected, defaulting to safe classification",
        "actions": ["Stay cautious"]
    }