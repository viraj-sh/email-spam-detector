from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from core.logging import setup_logging
from core.exceptions import handle_exception
from app.services.predict import predict_spam_labels
from schema.pydantic_predict import PredictSpamRequest, PredictSpamResponse


router = APIRouter(tags=["Model"])
logger = setup_logging(name="core.predict_spam_endpoint", level="INFO")


@router.post(
    "/predict",
    response_model=PredictSpamResponse,
    operation_id="predictSpamLabels",
    summary="Predict spam labels for email texts",
    description="Runs the spam classification model on provided email texts and returns prediction labels, confidence scores, and model metadata.",
)
async def predict_spam_endpoint(
    payload: PredictSpamRequest = Body(...),
) -> JSONResponse:
    try:
        logger.info("Received spam prediction request")
        result: Dict[str, Any] = predict_spam_labels(email_texts=payload.email_texts)
        return JSONResponse(content=result, status_code=result.get("status_code", 200))
    except Exception as exc:
        error_result = handle_exception(logger, exc, context="predict_spam_endpoint")
        return JSONResponse(
            content=error_result, status_code=error_result.get("status_code", 500)
        )
