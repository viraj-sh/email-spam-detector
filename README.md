## Model Training

Run the training pipeline:

python -m src.train

This will:
- Load and clean the dataset
- Perform TF-IDF + LinearSVC training
- Tune hyperparameters with GridSearchCV
- Save the trained model to /models
