from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  # Import accuracy_score here

class Trainer:
    def __init__(self, model, features, target):
        self.model = model
        self.X = features
        self.y = target

    # Function to split data into train and test sets
    def train_test_split(self):
        return train_test_split(self.X, self.y, test_size=0.2, shuffle=False)

    # Function to train and evaluate the model
    def train_and_evaluate(self):
        X_train, X_test, y_train, y_test = self.train_test_split()

        # Train the model (assuming the model has a fit method)
        self.model.fit(X_train, y_train)

        # Make predictions and evaluate the model
        y_pred = self.model.predict(X_test)

        # Calculate accuracy or other performance metrics
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

        return self.model  # Return the trained model for further use
