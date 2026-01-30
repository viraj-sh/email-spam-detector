import pandas as pd
from sklearn.model_selection import train_test_split
from .preprocessing import clean_text

def load_data(path: str):
    df = pd.read_csv(path)

    X = df['text'].apply(clean_text)
    y = df['label']

    X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.15, stratify=y, random_state=42)

    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.1765, stratify=y_temp, random_state=42)

    return X_train, X_val, X_test, y_train, y_val, y_test
