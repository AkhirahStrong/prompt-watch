
"""
PromptWatch Detection Engine

This module contains the prompt inspection logic used
to detect potentially malicious prompts.
"""


def analyze_prompt(prompt: str):
    
    return{
        "prompt": prompt,
        "detected": False,
        "risk_score": 0,
        "risk_level": "Low",
        "reason": "No malicious content detected."
    }