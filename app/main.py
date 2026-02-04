from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.system import router as system_router
from api.v1.predict import router as predict_router
from core.logging import setup_logging

logger = setup_logging(name="app", level="INFO")

app = FastAPI(title="Email Spam Detector API v1")

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:8000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Application startup complete")

# Include routers
app.include_router(system_router, prefix="/api/v1")
app.include_router(predict_router, prefix="/api/v1")
