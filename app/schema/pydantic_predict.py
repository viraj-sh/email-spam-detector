from pydantic import BaseModel, Field
from typing import List, Optional


class PredictSpamRequest(BaseModel):
    email_texts: List[str] = Field(
        ..., min_items=1, description="List of raw email texts to classify"
    )


class SpamPredictionItem(BaseModel):
    label: str
    decision_score: float
    model_inference_ms: float
    model_version: str
    text_length: int
    flag_low_confidence: bool


class PredictSpamData(BaseModel):
    predictions: List[SpamPredictionItem]


class PredictSpamResponse(BaseModel):
    success: bool
    error: Optional[str] = None
    data: Optional[PredictSpamData] = None
    status_code: int
