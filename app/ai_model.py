import joblib

# Load the trained model
model = joblib.load("model/model.pkl")


def predict_status(cpu, memory, disk):
    prediction = model.predict([[cpu, memory, disk]])
    return prediction[0]