from fastapi import APIRouter
from pydantic import BaseModel
from app.engine.detector import analyze_prompt

#Create a router that groups related API endpoints.
router = APIRouter()

#Define a Pydantic model for PRomptWatch API endpoints.
class PromptRequest(BaseModel):
    prompt: str
    # user_id: str
    # timestamp: str

#Accept a POST request to the /analyzer
@router.post("/analyzer")
async def analyze_prompt_route(request: PromptRequest):
   
    result = analyze_prompt(request.prompt)
    
    return result