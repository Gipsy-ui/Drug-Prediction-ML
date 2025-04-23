import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("mlapp/data/drug200.csv")

label_encoders = {}
for column in ["Sex", "BP", "Cholesterol", "Drug"]:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le 

# Split dataset
X = df.drop(columns=["Drug"])  # Part ng Features
y = df["Drug"]  # Part ng Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save ng preprocessed data
X_train.to_csv("mlapp/data/X_train.csv", index=False)
X_test.to_csv("mlapp/data/X_test.csv", index=False)
y_train.to_csv("mlapp/data/y_train.csv", index=False)
y_test.to_csv("mlapp/data/y_test.csv", index=False)

print("Data preprocessing completed!")
