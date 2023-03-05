import json
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routes import router


app_config = {
    "title": "molu-engine",
    "description": "Next Generation Wiki Engine",
    "version": "0.0.1",
    "redoc_url": "/docs/redoc",
    "docs_url": "/docs/swagger",
}

app = FastAPI(**app_config)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/")
