# FastAPI Request Counter

## Project Overview
This project is a **FastAPI-based Python application** that serves an HTTP route `/count`. It records and returns the total number of requests served, with persistence managed via a database.
![alt text](image.png)
***Figure 1: FastAPI Application /count Endpoint Response***
## Features
- **HTTP Route**: `/count` that responds with `{"count": "<int>"}`.
- **Database Integration**: Persists request counts.
- **Dockerized**: Simplifies deployment in containerized environments.
- **Kubernetes-ready**: Includes YAML manifests for cluster deployment.

---
## Deployment on AWS

This section covers deploying the application on AWS using various services to ensure scalability and high availability.

# Architecture Components
![alt text](<Blank diagram (2).png>)
***Figure 2: AWS services used for application deployment***
### **Users**
- End users interact with the application via HTTP requests.

### **Application Load Balancer (ALB)**
- Handles incoming traffic from users.
- Routes traffic to the Kubernetes cluster based on defined rules.
- Ensures high availability and load balancing for the application.

### **Amazon EKS (Elastic Kubernetes Service)**
- Hosts the Kubernetes cluster, which runs the application.
- Contains **Services** and **Pods**:
  - **Services**: Provide networking to expose the application within the cluster or externally via ALB.
  - **Pods**: Run the FastAPI application. They are the smallest deployable units in Kubernetes.

### **Amazon RDS (Relational Database Service)**
- Stores persistent data, in this case, the request counts.
- Ensures high availability and scalability for the database.

### **Amazon ECR (Elastic Container Registry)**
- Stores the Docker images of the FastAPI application.
- Kubernetes pulls the images from ECR to deploy the pods.

### **IAM (Identity and Access Management)**
- Manages access permissions between AWS services.
- Ensures the Kubernetes cluster, ALB, and RDS have the necessary roles and policies to interact securely.


By using these AWS services, the application can be deployed in a fully managed and scalable environment. The Kubernetes deployment ensures that the app can handle increased traffic, while the RDS database allows for persistent storage of request counts.

