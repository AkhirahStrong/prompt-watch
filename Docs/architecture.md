# PromptWatch Architecture

## Overview

PromptWatch is built incrementally to teach modern Python backend development and AI security architecture. Each module introduces one new software engineering concept while contributing to a working AI security application.

PromptWatch is an AI Prompt Injection Firewall designed to inspect user
prompts before they are sent to a Large Language Model (LLM).

The application uses a layered security architecture to normalize,
analyze, score, and respond to potentially malicious prompts.

---

# High-Level Architecture

```
React Frontend
        │
        ▼
FastAPI API
        │
        ▼
API Routes
        │
        ▼
Detection Engine
        │
 ┌──────┴──────┐
 ▼             ▼
Normalizer   Rule Engine
        │
        ▼
Risk Scoring
        │
        ▼
Analysis Result
        │
        ▼
JSON Response
```

---

# Module Responsibilities

| Module        | Purpose                                             | Project Dependencies       | External Dependencies |
| ------------- | --------------------------------------------------- | -------------------------- | --------------------- |
| main.py       | Starts the FastAPI application and registers routes | routes.py                  | FastAPI               |
| routes.py     | Receives HTTP requests and returns responses        | detector.py, response.py   | FastAPI, Pydantic     |
| detector.py   | Coordinates prompt analysis                         | normalizer.py, response.py | None                  |
| normalizer.py | Normalizes prompt text before analysis              | None                       | None                  |
| response.py   | Defines standardized API response models            | None                       | Pydantic              |

---

# Request Flow

1. User submits a prompt.
2. FastAPI receives the HTTP request.
3. PromptRequest validates the request body.
4. The route calls the detection engine.
5. The detector normalizes the prompt.
6. Detection rules inspect the normalized prompt.
7. A risk score is calculated.
8. An AnalysisResult object is created.
9. FastAPI returns the response as JSON.

---

# Current Project Status

## Phase 1 ✅

- Project Initialization
- FastAPI Backend
- React Frontend
- Request Models
- Response Models
- Detection Engine
- Prompt Normalization

## Phase 2 🚧

- Detection Rules
- Risk Scoring
- Rule Engine

## Future Phases

- Regex Detection
- Logging
- SQLite
- Dashboard
- Authentication
- AI Analysis
- Deployment
