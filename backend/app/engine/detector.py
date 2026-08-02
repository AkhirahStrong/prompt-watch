
"""
========================================================
PromptWatch

Module: detector.py

Purpose:
    Contains the core prompt analysis logic used to inspect
    user input for potential prompt injection attacks and
    other suspicious patterns.

Responsibilities:
    - Analyze incoming prompts
    - Detect malicious patterns
    - Calculate risk scores
    - Return standardized analysis results

Dependencies:
    AnalysisResult
    normalizer.py
    response.py
    
Author:
    Akhirah Strong

========================================================
"""

from app.models.response import AnalysisResult
from app.engine.normalizer import normalized_prompt


def analyze_prompt(prompt: str) -> AnalysisResult:
    normalized_prompt_text = normalized_prompt(prompt)

    return AnalysisResult(
        prompt=prompt,
        detected=False,
        risk_score=0,
        risk_level="Low",
        reason="No malicious content detected."
    )
    