from fastapi import FastAPI
from typing import Dict, Any
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from src.api.routes import agent_router
from src.api.search_routes import search_router


# Initialize App
app = FastAPI(
    title="Vidwaan AI Agent API",
    description="Agent-powered Q&A service for Vedic knowledge",
    version="1.0.0",
)

# CORS Configuration
# Allow frontend and backend to talk to Agent API
origins = [
    "http://localhost:3000",  # Frontend Dev
    "http://localhost:8000",  # Backend Dev
    "https://vidwaan.com",  # Prod
    "https://backend.vidwaan.com",  # Prod Backend
    "*",  # For now, allow all (MVP)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Custom OpenAPI Schema
def custom_openapi() -> Dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Vidwaan AI Agent API",
        version="1.0.0",
        description="API for querying Vedic knowledge via intelligent agent",
        routes=app.routes,
    )

    # Add servers for Swagger UI
    openapi_schema["servers"] = [
        {"url": "http://localhost:8001", "description": "Local Development Server"},
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore


@app.get("/", tags=["Health"])
async def root() -> Dict[str, str]:
    """Root endpoint to verify API is running."""
    return {"message": "Vidwaan AI Agent API is running", "docs_url": "/docs"}


app.include_router(agent_router)
app.include_router(search_router)
