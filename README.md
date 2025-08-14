# Course Enrollment Service

A full-stack course enrollment application built with Express.js frontend and Flask backend, containerized with Docker and MongoDB Atlas integration.

## Architecture Overview

This project consists of two main services that communicate over a shared Docker network:

**Frontend Service:** Express.js server serving HTML enrollment forms
**Backend Service:** Flask API handling data processing and MongoDB operations

## 🚀 Features

- Simple HTML course enrollment form
- Real-time form submission to backend API
- MongoDB Atlas cloud database integration
- Containerized microservices architecture
- Docker Compose orchestration

## 📋 Prerequisites

- Docker and Docker Compose installed
- MongoDB Atlas account and connection string
- Node.js (for local development)
- Python 3.x (for local development)

## 🛠️ Setup and Installation

Clone the Repository

```bash
    git clone <repository-url>
    cd course-enrollment-service
```

## 🐳 Docker Configuration

- Frontend Dockerfile (Dockerfile.front)
- Based on Node.js Alpine image
- Exposes port 3000
- Serves Express.js application
- Backend Dockerfile (Dockerfile.back)
- Based on Python Alpine image
- Exposes port 5000
- Runs Flask application
- Docker Compose Network
- Both services communicate over a shared Docker network (course-network) enabling seamless inter-service communication.

## 📝 Usage

- Navigate to <http://localhost:3000>
- Fill out the course enrollment form
- Submit the form
- Data is processed by Flask backend
- Enrollment information is stored in MongoDB Atlas
- Confirmation is displayed to the user

## 🛡️ Security Considerations

- Environment variables for sensitive data
- MongoDB connection string encryption
- Input validation on both frontend and backend
- CORS configuration for cross-origin requests

## 📚 Technologies Used

- Frontend: Express.js, HTML, CSS, JavaScript
- Backend: Flask, Python
- Database: MongoDB Atlas
- Containerization: Docker, Docker Compose
- Runtime: Node.js, Python

## 🤝 Contributing

- Fork the repository
- Create a feature branch
- Make your changes
- Add tests if applicable
- Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
