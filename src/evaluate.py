from sklearn.metrics import classification_report, confusion_matrix

def evaluate(model, x_test, y_test):
    predictions = model.predict(x_test)
    print(classification_report(y_test, predictions))
    print(confusion_matrix(y_test, predictions))