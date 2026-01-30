import joblib 
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from .data_loader import load_data

def build_pipeline():
    return Pipeline([
        ('tf-idf', TfidfVectorizer(stop_words='english', max_df=0.95, min_df=5, ngram_range=(1, 2), sublinear_tf=True)),
        ('clf', LinearSVC(class_weight='balanced'))
    ])

def get_param_grid():
    return {
        'tf-idf__max_df': [0.9, 0.95],
        'tf-idf__min_df': [3, 5],
        'tf-idf__ngram_range': [(1, 1), (1, 2)],
        'clf__C': [0.5, 1, 2],
    }

def train(data_path:str, model_output_path: str):
    X_train, X_val, X_test, y_train, y_val, y_test = load_data(data_path)
    
    X_final_train = pd.concat([X_train, X_val])
    y_final_train = pd.concat([y_train, y_val])

    pipeline = build_pipeline()
    param_grid = get_param_grid()

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    grid = GridSearchCV(pipeline, param_grid, cv=cv, scoring='f1', n_jobs=-1, verbose=2)

    grid.fit(X_final_train, y_final_train)

    best_model = grid.best_estimator_

    X_all = pd.concat([X_final_train, X_test])
    y_all = pd.concat([y_final_train, y_test])
    best_model.fit(X_all, y_all)

    joblib.dump(best_model, model_output_path)
    print(f"Model saved to {model_output_path}")


if __name__ == "__main__":
    train('data/email_text.csv', 'models/spam_classifier.joblib')