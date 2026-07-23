from fastapi import FastAPI
from app.monitor import get_system_metrics
from app.database import create_database, save_metrics, get_history
from app.ai_model import predict_status

app = FastAPI(
    title="AI Infrastructure Monitoring Platform",
    version="1.0.0"
)

# Create the database when the application starts
create_database()


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Infrastructure Monitoring Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }


@app.get("/metrics")
def metrics():
    metrics = get_system_metrics()

    save_metrics(
        metrics["cpu_usage"],
        metrics["memory_usage"],
        metrics["disk_usage"]
    )

    return metrics


@app.get("/history")
def history():
    data = get_history()

    history_data = []

    for row in data:
        history_data.append({
            "id": row[0],
            "cpu": row[1],
            "memory": row[2],
            "disk": row[3],
            "created_at": row[4]
        })

    return history_data


@app.get("/predict")
def predict():

    metrics = get_system_metrics()

    prediction = predict_status(
        metrics["cpu_usage"],
        metrics["memory_usage"],
        metrics["disk_usage"]
    )

    return {
        "cpu_usage": metrics["cpu_usage"],
        "memory_usage": metrics["memory_usage"],
        "disk_usage": metrics["disk_usage"],
        "prediction": prediction
    }