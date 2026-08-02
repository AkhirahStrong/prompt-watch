"""
========================================================
PromptWatch

Module: routes.py

Purpose:
    Defines the FastAPI routes used to receive prompt
    analysis requests and return analysis results.

Responsibilities:
    - Define API endpoints
    - Validate incoming request data
    - Pass prompts to the detection engine
    - Return standardized analysis responses
    - Connect HTTP requests to PromptWatch business logic

Dependencies:
    - FastAPI
    - Pydantic
    - PromptWatch detection engine
    - PromptWatch response models

Author:
    Akhirah Strong

========================================================
"""

from fastapi import APIRouter
from pydantic import BaseModel
from app.engine.detector import analyze_prompt
from backend.app.models.response import AnalysisResult

#Create a router that groups related API endpoints.
router = APIRouter()

#Define a Pydantic model for PRomptWatch API endpoints.
class PromptRequest(BaseModel):
    prompt: str
    # user_id: str
    # timestamp: str

#Accept a POST request to the /analyzer
@router.post("/analyzer", response_model=AnalysisResult)
async def analyze_prompt_route(request: PromptRequest):
   
    result = analyze_prompt(request.prompt)
    
    return result