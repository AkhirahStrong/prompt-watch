"""
========================================================
PromptWatch

Module: response.py

Purpose:
    Defines the standardized response models returned by
    the PromptWatch API after prompt analysis.

Responsibilities:
    - Define API response schemas
    - Validate response data
    - Document response structure for FastAPI

Dependencies:
    - Pydantic

Author:
    Akhirah Strong

========================================================
"""

from pydantic import BaseModel

class AnalysisResult(BaseModel):
    
    #This is the result of a prompt analyzation.
    prompt: str
    detected: bool
    risk_score: int
    risk_level: str
    reason: str
    # analysis: dict
    
    