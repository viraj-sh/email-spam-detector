import json
import joblib

def save_label_mapping(path = 'models/label_mapping.joblib'):
    label_map = {0: 'ham', 1: 'spam'}
    joblib.dump(label_map, path)

def save_metadata(metadata: dict, path='models/model_metadata.json'):
    with open(path, 'w') as f:
        json.dump(metadata, f, indent=4)