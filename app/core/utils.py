from typing import Any, Optional
import re
import os
import sys

def resource_path(relative_path: str):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

MODEL_PATH = resource_path("app/model/spam_classifier_v1.joblib")
LABEL_MAPPING_PATH = resource_path("app/model/label_mapping_v1.joblib")

# ASCII COLORS
RESET = "\033[0m"
BOLD = "\033[1m"
FG_RED = "\033[31m"
FG_WHITE = "\033[97m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"


def standard_response(
    success: bool,
    error: Optional[str] = None,
    data: Optional[Any] = None,
    status_code: int | None = None,
) -> dict[str, Any]:
    return {
        "success": bool(success),
        "error": error if not success else None,
        "data": data if success else None,
        "status_code": status_code,
    }


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
