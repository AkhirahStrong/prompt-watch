from fastapi import APIRouter

#Create a router that groups related API endpoints.
router = APIRouter()

#Accept a POST request to the /analyzer
@router.post("/analyzer")
async def analyze_prompt():
    #Temporary for testing if the endpoint works.
    return {
        "message": "Prompt analysis endpoint is working!"}