from sklearn.tree import DecisionTreeClassifier
import joblib

# Training data
X = [
    [10, 20, 30],
    [15, 25, 35],
    [25, 35, 40],
    [35, 45, 50],
    [45, 55, 60],
    [60, 65, 70],
    [70, 75, 80],
    [80, 85, 90],
    [90, 95, 95],
    [95, 98, 99]
]

# Labels
y = [
    "Normal",
    "Normal",
    "Normal",
    "Normal",
    "Normal",
    "High Load",
    "High Load",
    "Critical",
    "Critical",
    "Critical"
]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, "model/model.pkl")

print("AI model trained successfully!")