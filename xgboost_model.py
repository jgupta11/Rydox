import xgboost as xgb
from sklearn.metrics import accuracy_score  # Import accuracy_score for model evaluation

class XGBoostModel:
    def __init__(self):
        self.model = xgb.XGBClassifier()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)  # Evaluate accuracy using accuracy_score
        print(f"Accuracy: {accuracy:.2f}")
