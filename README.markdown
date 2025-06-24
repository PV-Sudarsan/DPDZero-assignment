# DevOps Intern Assignment: Nginx Reverse Proxy + Docker

This project sets up a Docker Compose-based system with an Nginx reverse proxy routing requests to two backend services (Golang and Python applications).

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PV-Sudarsan/DPDZero-assignment.git
   cd DPDZero-assignment
   ```

2. **Build and Run**:
   Run the following command to build and start all services:
   ```bash
   docker-compose up --build
   ```

3. **Access the Services**:
   - Service 1: `http://localhost/service1/ping`
   - Service 2: `http://localhost/service2/ping`
   **or**
   - Service 1: `http://localhost/service1/hello`
   - Service 2: `http://localhost/service2/hello`
   

## How Routing Works

- **Nginx Reverse Proxy**:
  - Listens on port `80`.
  - Routes requests with `/service1` prefix to the Golang service running on `service1:8001`.
  - Routes requests with `/service2` prefix to the Python service running on `service2:8002`.
  - Logs incoming requests with timestamp, path, and other details to `/var/log/nginx/access.log`.

- **Networking**:
  - Uses a bridge network (`app-network`) to allow communication between containers.
  - Services are isolated and only accessible via the Nginx proxy on port `80`.

## Bonus Features

- **Health Checks**:
  - Configured in `docker-compose.yml` with a 30s interval, 10s timeout, and 3 retries.

- **Logging**:
  - Nginx logs requests with a custom format including timestamp, request path, status, and more.
  - View logs using:
    ```bash
    docker-compose logs nginx
    ```

- **Clean Docker Setup**:
  - Modular Dockerfiles for each service.
  - Lightweight base images (`nginx:alpine`, `golang:1.21-alpine`, `python:3.11-slim`).
  - Single command (`docker-compose up --build`) to run the system.

## Testing

- Verify routing:
  ```bash
  curl http://localhost/service1
  curl http://localhost/service2
  ```
- Check Nginx logs:
  ```bash
  docker-compose logs nginx
  ```