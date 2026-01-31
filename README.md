## Model Training

The training workflow is provided as a notebook for one-time model training and experimentation.

Open and run:

notebooks/spam_training_pipeline.ipynb

This notebook will:
- Load and clean the dataset from /dataset
- Perform TF-IDF + LinearSVC training
- Tune hyperparameters using GridSearchCV
- Save the trained model to app/model/