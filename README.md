## 📌 Project Overview

**Honeypot-as-a-Service (HaaS)** is a **containerized and automated honeypot system** designed to capture, analyze, and provide actionable insights into cyber threats. The system enables organizations to deploy honeypots dynamically, collect attack data, and visualize threat patterns via an interactive web dashboard.

This project integrates **FastAPI, PostgreSQL, Docker, and DevOps principles** to automate deployment, monitoring, and scaling. 

## Features
- **Real-time Threat Monitoring:** Capture malicious activities and visualize them.
- **API-based Data Retrieval:** Fetch honeypot logs and attack patterns.
- **Web Dashboard:** View and analyze captured threats in a user-friendly interface.
- **DevOps Integration:** Automated deployment with **GitHub Actions & Docker-based CI/CD pipelines**.
- **Scalability & Containerization:** Deploy multiple honeypots effortlessly using Docker.

---

## 📂 Project Structure
```
honeypot-as-a-service/
│── app/
│   ├── __init__.py            # Package initializer
│   ├── main.py                # FastAPI entry point
│   ├── config.py              # Configuration settings
│   ├── database.py            # Database setup
│   ├── models.py              # Database models
│   ├── auth.py                # Authentication functions
│   ├── honeypot.py            # Honeypot logic
│   ├── schemas.py             # Pydantic models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user_routes.py
│   │   ├── honeypot_routes.py
│── templates/                 # Jinja2 templates for the web dashboard
│── migrations/                 # Database migration files
│── tests/                      # Unit and integration tests
│── docker-compose.yaml         # Docker Compose setup
│── Dockerfile                  # Docker image build file
│── requirements.txt            # Python dependencies
│── README.md                   # Project documentation
```

---

## Setup and Installation

### **Prerequisites**
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL (if not using Docker)
- Git

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Vaibhav27072004/Haas-Threat_Intelligence.git
cd honeypot-as-a-service
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Setup Environment Variables**
Create a `.env` file and configure database settings:
```
DATABASE_URL=postgresql://user:password@db/honeypot
SECRET_KEY=your_secret_key
```

### **4️⃣ Run the Application (Locally)**
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### **5️⃣ Run with Docker**
```sh
docker-compose up --build
```

The service should now be running at: **http://localhost:8000**

---

## 🌍 API Endpoints

| Endpoint                 | Method | Description |
|--------------------------|--------|-------------|
| `/api/status`            | GET    | Check service health |
| `/api/users`             | POST   | Register a new user |
| `/api/honeypot`          | POST   | Log a honeypot event |
| `/api/honeypot`          | GET    | Fetch all attack logs |
| `/dashboard`             | GET    | View web dashboard |

### **Example: Logging an Attack**
```sh
curl -X POST "http://localhost:8000/api/honeypot" \
     -H "Content-Type: application/json" \
     -d '{"attacker_ip": "192.168.1.10", "attack_type": "SQL Injection"}'
```

---

## 📊 Web Dashboard
The web dashboard provides **real-time visualization** of collected attack data. Access it at:
```sh
http://localhost:8000/dashboard
```

---

## 🔄 DevOps Integration
This project leverages **GitHub Actions** and **Docker** for CI/CD.

### **CI/CD Workflow**
- **GitHub Actions:** Automates build, test, and deployment.
- **Docker Compose:** Deploys the application and database as containers.
- **PostgreSQL Logging:** Stores attack data for analysis.

### **Running Tests**
```sh
pytest tests/
```

---

## 🚀 Future Enhancements
- **Machine Learning Integration** for advanced threat detection.
- **Multi-Cloud Support** (AWS, Azure, GCP).
- **SIEM Integration** with enterprise security tools.

---

## 🛠️ Contributing
Feel free to contribute by forking the repository and submitting pull requests.

---

## 📜 License
This project is licensed under the **MIT License**.

---



