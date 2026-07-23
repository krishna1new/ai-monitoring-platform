# 🚀 AI Infrastructure Monitoring Platform

An AI-powered Infrastructure Monitoring Platform built with **FastAPI**, **Python**, **Docker**, and **Machine Learning** to monitor system resources, store historical metrics, and predict infrastructure health.

---

## 📌 Overview

This project collects real-time system metrics such as CPU, Memory, and Disk usage using **psutil**, stores them in a database, and uses a Machine Learning model to predict the health status of the system.

The application is containerized with Docker and can be deployed locally or on cloud platforms like AWS.

---

## ✨ Features

* 📊 Real-time infrastructure monitoring
* 💻 CPU, Memory, and Disk usage tracking
* 🤖 AI-based system health prediction
* 🗄️ Historical metrics storage
* ⚡ REST API built with FastAPI
* 🐳 Dockerized application
* 📦 Docker Compose support
* ☁️ Ready for cloud deployment

---

## 🛠️ Tech Stack

### Backend

* Python 3
* FastAPI
* Uvicorn

### Monitoring

* psutil

### Machine Learning

* scikit-learn
* Joblib

### Database

* SQLite

### DevOps

* Docker
* Docker Compose
* Git & GitHub

---

## 📁 Project Structure

```text
ai-monitoring-platform/
│
├── app/
│   ├── main.py
│   ├── monitor.py
│   ├── database.py
│   └── ai_model.py
│
├── data/
│
├── model/
│   └── model.pkl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── train_model.py
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/krishna1new/ai-monitoring-platform.git

cd ai-monitoring-platform
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

## 🐳 Run with Docker

Build the image:

```bash
docker build -t ai-monitoring-platform .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name ai-monitoring-container ai-monitoring-platform
```

---

## 🐳 Run with Docker Compose

Start:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

---

## 📡 API Endpoints

| Method | Endpoint   | Description                       |
| ------ | ---------- | --------------------------------- |
| GET    | `/`        | Welcome message                   |
| GET    | `/health`  | Application health check          |
| GET    | `/metrics` | Current system metrics            |
| GET    | `/history` | Historical monitoring data        |
| GET    | `/predict` | AI-based system health prediction |

---

## 🤖 Machine Learning

The platform uses a **Decision Tree Classifier** trained on infrastructure metrics.

Model inputs:

* CPU Usage
* Memory Usage
* Disk Usage

Output:

* Healthy
* Warning
* Critical

---

## 🔮 Future Enhancements

* PostgreSQL support
* Prometheus integration
* Grafana dashboard
* Authentication & Authorization
* Email and Slack alerts
* Kubernetes deployment
* GitHub Actions CI/CD
* AWS EC2 deployment
* Real-time monitoring dashboard

---

## 👨‍💻 Author

**Krishna Yadav**

* GitHub: https://github.com/krishna1new
* LinkedIn: [www.linkedin.com/in/krishnayadavba](http://www.linkedin.com/in/krishnayadavba)

---

## 📄 License

This project is licensed under the MIT License.
