# FastAPI Request Counter

## Project Overview
This project is a **FastAPI-based Python application** that serves an HTTP route `/count`. It records and returns the total number of requests served, with persistence managed via a database.

## Features
- **HTTP Route**: `/count` that responds with `{"count": "<int>"}`.
- **Database Integration**: Persists request counts.
- **Dockerized**: Simplifies deployment in containerized environments.
- **Kubernetes-ready**: Includes YAML manifests for cluster deployment.

---
## Deployment on AWS

This section covers deploying the application on AWS using various services to ensure scalability and high availability.

### AWS Services Needed

To deploy the application on AWS, the following services are required:

- **Elastic Kubernetes Service (EKS)**: To host the FastAPI application and provide a scalable Kubernetes cluster.
- **Amazon RDS**: To store the request count in a database.
- **Application Load Balancer (ALB)**: To distribute incoming traffic to the Kubernetes cluster.
- **IAM Roles**: To grant the necessary permissions for interacting with AWS services.
- **Elastic Container Registry (ECR)**: For storing the Docker images used in the Kubernetes deployment.

![alt text](<Blank diagram (2).png>)
**Figure 1: AWS services used for application deployment**

By using these AWS services, the application can be deployed in a fully managed and scalable environment. The Kubernetes deployment ensures that the app can handle increased traffic, while the RDS database allows for persistent storage of request counts.

