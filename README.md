# Flask Docker CI/CD Project

A production-ready Flask application with Docker containerization and complete CI/CD pipeline using GitHub Actions.

## Features

- 🐳 Docker containerization
- 🔄 Multi-stage builds for optimization
- 🧪 Automated testing with pytest
- 🚀 CI/CD with GitHub Actions
- 🔒 Security scanning with Trivy
- 📊 Health checks and monitoring
- 🔄 Blue-green deployment support
- ↩️ Rollback capability
- 🗄️ PostgreSQL database
- ⚡ Redis caching
- 🌐 Nginx reverse proxy

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git

### Local Development

1. **Clone and setup:**
```bash
   git clone <your-repo-url>
   cd flask-docker-cicd
   cp .env.example .env
```

2. **Start services:**
```bash
   docker-compose up -d
```

3. **Access:**
   - Flask App: http://localhost:5000
   - Database Admin: http://localhost:8080
   - API Health: http://localhost:5000/health

4. **Run tests:**
```bash
   docker-compose exec web pytest -v
```

## API Endpoints

- `GET /` - Home
- `GET /health` - Health check
- `GET /add/<a>/<b>` - Addition
- `GET /subtract/<a>/<b>` - Subtraction
- `GET /multiply/<a>/<b>` - Multiplication

## CI/CD Setup

### 1. Update Docker Hub Username

Replace `your-dockerhub-username` in:
- `.github/workflows/build.yml`
- `.github/workflows/deploy.yml`
- `.github/workflows/rollback.yml`
- `docker-compose.prod.yml`

### 2. Add GitHub Secrets

Go to: Settings → Secrets and variables → Actions

Add these secrets:
- `DOCKER_USERNAME` - Your Docker Hub username
- `DOCKER_TOKEN` - Docker Hub access token
- `SERVER_HOST` - Production server IP (optional, for deployment)
- `SERVER_USER` - SSH username (optional)
- `SSH_PRIVATE_KEY` - SSH private key (optional)

### 3. Get Docker Hub Access Token

1. Go to https://hub.docker.com
2. Click on your profile → Account Settings
3. Security → New Access Token
4. Copy the token and add to GitHub Secrets as `DOCKER_TOKEN`

## Workflows

### CI (Continuous Integration)
**Triggers:** Push to main/develop, Pull requests
- Runs tests
- Code linting
- Security scanning

### Build and Push
**Triggers:** Push to main, Version tags
- Builds Docker image
- Pushes to Docker Hub
- Tags with version/SHA

### Deploy (Optional)
**Triggers:** After successful build
- Deploys to production server via SSH

### Rollback (Manual)
**Trigger:** Manual dispatch
- Rollback to specific version

## Development Workflow

1. Create feature branch:
```bash
   git checkout -b feature/my-feature
```

2. Make changes and test locally:
```bash
   docker-compose up -d
   docker-compose exec web pytest -v
```

3. Commit and push:
```bash
   git add .
   git commit -m "Add feature"
   git push origin feature/my-feature
```

4. Create Pull Request on GitHub
5. CI runs automatically
6. Merge to main → Automatic build and deploy

## Creating Releases
```bash
git tag v1.0.0
git push origin v1.0.0
```

This creates:
- `flask-app:v1.0.0`
- `flask-app:1.0`
- `flask-app:latest`

## Project Structure
```
flask-docker-cicd/
├── .github/workflows/      # CI/CD pipelines
│   ├── ci.yml
│   ├── build.yml
│   ├── deploy.yml
│   └── rollback.yml
├── app/                    # Application code
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── test_app.py
├── docker-compose.yml      # Development
├── docker-compose.prod.yml # Production
├── nginx.conf
└── README.md
```

## Troubleshooting

### View logs
```bash
docker-compose logs -f web
```

### Check container status
```bash
docker-compose ps
```

### Restart services
```bash
docker-compose restart
```

### Clean up
```bash
docker-compose down -v
docker system prune -a
```

## License

MIT
