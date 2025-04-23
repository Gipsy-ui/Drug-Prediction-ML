import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load ng preprocessed data
X_train = pd.read_csv("mlapp/data/X_train.csv")
y_train = pd.read_csv("mlapp/data/y_train.csv")

# Train ng RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train.values.ravel())  #  Part ng`.ravel()` to avoid warnings

# Save ng trained model
joblib.dump(model, "mlapp/model.pkl")

print("Model training completed and saved as model.pkl!")
