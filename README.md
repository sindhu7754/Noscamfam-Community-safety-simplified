NoScamFam — Community Safety & Digital Wellness Platform

A lightweight, AI-assisted incident processing system designed to transform unstructured community safety reports into structured, prioritized, and actionable security insights.

Candidate Name

Prathima Sindhu Varshini Sabbi

Scenario Chosen

Community Safety & Digital Wellness

Estimated Time Spent

~3.5 hours

1. Problem Overview

Modern users face an overwhelming volume of fragmented safety information from social platforms, messaging apps, and informal channels. This leads to:

Alert fatigue

Lack of actionable guidance

Difficulty distinguishing real threats from noise

NoScamFam addresses this by converting raw incident descriptions into structured intelligence, prioritizing threats, and delivering clear, calm, and actionable recommendations.

2. System Architecture

The system is designed as a modular processing pipeline:

User Input (UI / API)
        ↓
Input Validation
        ↓
Normalization
        ↓
Classification (AI Module)
        ↓
Fallback Rule Engine
        ↓
Risk Scoring Engine
        ↓
Duplicate Detection
        ↓
Storage (JSON)
        ↓
Query / Search Layer
        ↓
Security Digest Generation

This architecture ensures clarity, reliability, and extensibility.

3. AI Integration and Fallback Strategy
AI Capability Implemented

Categorization (phishing, credential attack, noise, unknown)

Summarization

Action recommendation

Implementation Approach

The current prototype uses a rule-based classification module (ai_module.py) that simulates structured AI output, including:

Type

Severity

Confidence score

Explanation

Recommended actions

Production Extension

In a production system, this module can be replaced with:

OpenAI GPT-based classification (e.g., GPT-4o-mini)

Prompt-based structured extraction

Fallback Mechanism

If the AI module fails or returns no result:

A deterministic rule-based fallback (fallback.py) is triggered

Provides safe defaults with lower confidence

This ensures system reliability under uncertainty, which is critical in real-world security systems.

4. Core Features
4.1 Incident Processing (End-to-End Flow)

POST /add — Submit incident → processed through full pipeline

GET /incidents — Retrieve all incidents

PUT /update/<id> — Update incident status

GET /search?q= — Filter incidents

4.2 Risk Scoring Engine

Each incident is assigned a risk score based on:

Severity

Presence of high-risk keywords

Frequency of similar incidents

Factor	Contribution
High severity	+5
Medium severity	+3
Low severity	+1
Keyword boost	+2
Repetition boost	+2

Output:

Score

Risk Level (LOW / MEDIUM / HIGH)

4.3 Noise-to-Signal Filtering

Non-actionable or emotional content is filtered:

Example: “angry”, “hate” → classified as noise

This directly addresses the problem of alert fatigue.

4.4 Duplicate Detection

A similarity-based mechanism identifies repeated incidents:

Uses word overlap ratio (>30%)

Prevents redundant signals from inflating perceived risk

4.5 Security Digest

The /digest endpoint provides a summarized, calm overview:

Total incidents

Risk distribution

Top recommended action

Example:

Enable 2FA immediately due to repeated phishing attempts

This design prioritizes clarity over volume, reducing user anxiety.

5. Responsible AI Considerations

The system is designed with a strong emphasis on responsible AI:

AI outputs are not blindly trusted

Fallback ensures deterministic behavior

Confidence scores provide transparency

Explanation field enables interpretability

Noise filtering reduces misinformation impact

6. Data Safety and Security

Synthetic data only (no real user data)

No external data scraping

No API keys committed to repository

.env used for environment configuration

Input validation enforced on all endpoints

7. Tech Stack
Layer	Technology
Backend	Python, Flask
AI Module	Rule-based classifier (AI simulation)
Storage	JSON file
Frontend	HTML, JavaScript (Fetch API)
Testing	Python (requests)
8. Testing

Two test cases are implemented:

Happy path — Valid incident submission

Edge case — Empty input validation

These ensure correctness of core functionality.

9. Tradeoffs and Design Decisions
What was intentionally simplified:

Real LLM integration → replaced with deterministic simulation

Database → JSON used for simplicity

Real-time streaming → omitted

Advanced UI → deprioritized

Rationale:

Focus was placed on:

system design

reliability

clear AI integration

meeting all functional requirements within time constraints

10. Future Enhancements

Integration with LLM APIs (OpenAI)

Database migration (PostgreSQL / SQLite)

Real-time ingestion (Kafka / WebSockets)

Safe Circles (secure group sharing)

Geographic visualization of incidents

11. Known Limitations

Classification is keyword-based (not full NLP)

JSON storage is not scalable for concurrent access

Similarity detection is lexical, not semantic

No rate limiting on endpoints

12. AI Disclosure

AI tools were used for ideation and structuring

All logic was manually verified through testing

Some suggestions were modified to improve reliability and determinism

13. Quick Start
Prerequisites

Python 3.8+

Run
pip install flask python-dotenv
python app.py

Open:

http://127.0.0.1:5000
Tests
python test_core.py
14. Sample Data

A synthetic dataset is provided in:

data/sample_data.json
15. Video Demonstration

[Add your public video link here]