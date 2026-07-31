from fastapi import FastAPI
from app.api.routes import router



# Create an instance (object) of the FastAPI application.
# This 'app' object is the main application that receives and processes
# incoming HTTP requests.
app = FastAPI(
    # The title displayed in the Swagger documentation (/docs).
    title="PromptWatch API",
    description="AI Prompt Security Gateway",
    version="1.0.0",
)

#Register the routes defined in app/api/routes.py.
app.include_router(router)

# Public health-check endpoint.
@app.get("/") 

# 'async' allows this function to handle requests efficiently.
async def root():
    return {
        "application": "PromptWatch",
        "status": "Running",
        "version": "1.0.0"
    }