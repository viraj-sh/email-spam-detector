from typing import Any, Dict, List
import time
import joblib
import os

from core.utils import standard_response
from core.logging import setup_logging
from core.exceptions import handle_exception
from app.core.utils import clean_text, MODEL_PATH, LABEL_MAPPING_PATH

logger = setup_logging(name="core.predict_spam_labels", level="INFO")


def predict_spam_labels(email_texts: List[str]) -> Dict[str, Any]:
    try:
        if not email_texts:
            logger.warning("Empty email_texts list received")
            return standard_response(
                False,
                error="No input texts provided",
                status_code=400,
            )

        logger.info("Loading spam classification model and label mapping")
        spam_classifier_model = joblib.load(MODEL_PATH)
        label_mapping: Dict[Any, str] = joblib.load(LABEL_MAPPING_PATH)

        logger.info("Cleaning input texts before inference")
        cleaned_texts: List[str] = [clean_text(text) for text in email_texts]

        model_version: str = os.path.basename(MODEL_PATH).replace(".joblib", "")

        logger.info("Starting model inference")
        start_time: float = time.perf_counter()

        raw_predictions = spam_classifier_model.predict(cleaned_texts)
        decision_scores = spam_classifier_model.decision_function(cleaned_texts)

        end_time: float = time.perf_counter()
        inference_time_ms: float = (end_time - start_time) * 1000

        logger.info("Model inference completed successfully")

        results: List[Dict[str, Any]] = []

        for index, cleaned in enumerate(cleaned_texts):
            score: float = float(decision_scores[index])
            label_key = raw_predictions[index]
            label: str = label_mapping.get(label_key, str(label_key))

            results.append(
                {
                    "label": label,
                    "decision_score": score,
                    "model_inference_ms": inference_time_ms,
                    "model_version": model_version,
                    "text_length": len(cleaned),
                    "flag_low_confidence": -0.5 <= score <= 0.5,
                    "input_text": email_texts[index],
                    "cleaned_text": cleaned,
                }
            )

        logger.info("Returning successful spam prediction response")
        return standard_response(
            True,
            data={"predictions": results},
            status_code=200,
        )

    except Exception as exc:
        return handle_exception(logger, exc, context="predict_spam_labels")
