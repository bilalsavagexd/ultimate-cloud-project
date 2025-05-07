# Ultimate Cloud Project

A secure, scalable cloud-native application deployed on AWS using modern DevOps practices.

## Architecture

The project implements a secure, scalable architecture using:
- AWS ECS (Fargate) for container orchestration
- Application Load Balancer for traffic distribution
- VPC with public and private subnets
- NAT Gateway for private subnet internet access
- CloudWatch for monitoring and logging
- ECR for container registry
- GitHub Actions for CI/CD

## Security Features

- Secret scanning with TruffleHog
- Dependency scanning with Snyk
- Security headers with Flask-Talisman
- Non-root container user
- Private subnet deployment
- HTTPS enforcement
- Content Security Policy
- Regular security updates

## Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured
- Docker installed
- Python 3.9+
- Terraform 1.0.0+

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ultimate-cloud-project
   ```

2. Configure AWS credentials:
   ```bash
   aws configure
   ```

3. Initialize Terraform:
   ```bash
   cd terraform
   terraform init
   ```

4. Apply Terraform configuration:
   ```bash
   terraform plan
   terraform apply
   ```

5. Build and push the Docker image:
   ```bash
   cd ../app
   docker build -t app .
   aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.eu-west-2.amazonaws.com
   docker tag app:latest <aws-account-id>.dkr.ecr.eu-west-2.amazonaws.com/app:latest
   docker push <aws-account-id>.dkr.ecr.eu-west-2.amazonaws.com/app:latest
   ```

## Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

3. Run tests:
   ```bash
   pytest app/test_app.py
   ```

4. Run locally:
   ```bash
   python app/app.py
   ```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

1. Security Scan:
   - TruffleHog for secret scanning
   - Snyk for dependency scanning

2. Testing:
   - Unit tests with pytest
   - Code coverage reporting

3. Build and Push:
   - Docker image build
   - Push to ECR

4. Deploy:
   - Update ECS task definition
   - Deploy to ECS Fargate

## Monitoring

- CloudWatch Logs for application logs
- CloudWatch Metrics for performance monitoring
- Container Insights for ECS monitoring

## Security Best Practices

1. Infrastructure:
   - Private subnets for application containers
   - Public subnets only for ALB and NAT Gateway
   - Security groups with least privilege
   - IAM roles with minimal permissions

2. Application:
   - Security headers
   - HTTPS enforcement
   - Non-root container user
   - Regular dependency updates

3. CI/CD:
   - Secret scanning
   - Dependency scanning
   - Automated testing
   - Manual approval for production deployments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 