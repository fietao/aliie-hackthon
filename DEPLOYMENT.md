# GrocerySort Deployment Guide

Complete guide to deploying GrocerySort to various platforms.

## Table of Contents
- [Local Development](#local-development)
- [Production Setup](#production-setup)
- [Docker Deployment](#docker-deployment)
- [Cloud Deployment](#cloud-deployment)
- [Performance Optimization](#performance-optimization)
- [Monitoring & Logging](#monitoring--logging)

## Local Development

### Prerequisites
- Python 3.8+
- pip
- Git

### Setup

1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd aliie-hackthon
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run application**
   ```bash
   python app.py
   ```

4. **Access**
   - Open browser: http://localhost:5000

### Development Tips
- Use `FLASK_DEBUG=True` for auto-reload
- Check browser console for errors (F12)
- Use Chrome DevTools for UI debugging

## Production Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install production dependencies**
   ```bash
   pip install -r requirements.txt
   pip install gunicorn
   ```

3. **Set environment variables**
   ```bash
   export FLASK_DEBUG=False
   export PORT=5000
   export HOST=0.0.0.0
   ```

### Running with Gunicorn (Recommended)

```bash
# Basic
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# With SSL
gunicorn -w 4 -b 0.0.0.0:443 --certfile=cert.pem --keyfile=key.pem app:app

# With systemd socket activation
gunicorn -w 4 --bind unix:/run/gunicorn.sock app:app
```

### Systemd Service (Linux)

Create `/etc/systemd/system/grocerysort.service`:

```ini
[Unit]
Description=GrocerySort Service
After=network.target

[Service]
Type=notify
User=www-data
WorkingDirectory=/home/www-data/aliie-hackthon
ExecStart=/home/www-data/aliie-hackthon/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl enable grocerysort
sudo systemctl start grocerysort
```

## Docker Deployment

### Build Image

```bash
docker build -t grocerysort:latest .
```

### Run Container

```bash
# Basic
docker run -p 5000:5000 grocerysort:latest

# With environment variables
docker run -p 5000:5000 \
  -e FLASK_DEBUG=False \
  -e PORT=5000 \
  grocerysort:latest

# Background with restart policy
docker run -d \
  --name grocerysort \
  --restart unless-stopped \
  -p 5000:5000 \
  grocerysort:latest
```

### Docker Compose

```bash
docker-compose up -d
```

View logs:
```bash
docker-compose logs -f
```

## Cloud Deployment

### Heroku

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create app**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **View logs**
   ```bash
   heroku logs --tail
   ```

### AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize**
   ```bash
   eb init -p python-3.11 grocerysort
   ```

3. **Create environment**
   ```bash
   eb create grocerysort-env
   ```

4. **Deploy**
   ```bash
   eb deploy
   ```

### Google Cloud Platform (Cloud Run)

1. **Build and push to Container Registry**
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT_ID/grocerysort
   ```

2. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy grocerysort \
     --image gcr.io/PROJECT_ID/grocerysort \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

### DigitalOcean App Platform

1. Push to GitHub
2. Connect repository to DigitalOcean
3. Configure app (Flask on port 5000)
4. Deploy

### Azure App Service

1. **Create resource group**
   ```bash
   az group create --name grocerysort-rg --location eastus
   ```

2. **Create App Service plan**
   ```bash
   az appservice plan create --name grocerysort-plan \
     --resource-group grocerysort-rg \
     --is-linux --sku F1
   ```

3. **Create app**
   ```bash
   az webapp create --resource-group grocerysort-rg \
     --plan grocerysort-plan \
     --name grocerysort-app \
     --runtime "python|3.11"
   ```

## Reverse Proxy Setup

### Nginx

```nginx
upstream grocerysort {
    server 127.0.0.1:5000;
}

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://grocerysort;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Apache

```apache
<VirtualHost *:80>
    ServerName example.com
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/
</VirtualHost>
```

## SSL/TLS Setup

### Let's Encrypt with Certbot

```bash
sudo certbot certonly --standalone -d example.com
```

Update Nginx/Apache to use certificates.

## Performance Optimization

### Caching
```python
@app.after_request
def add_cache_headers(response):
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response
```

### Compression
```bash
pip install Flask-Compress
```

### Database Connection Pooling
(If using database in future)

## Monitoring & Logging

### Application Logs
```bash
# View logs
tail -f logs/app.log

# Rotate logs
logrotate -f /etc/logrotate.d/grocerysort
```

### Health Checks
```bash
curl http://localhost:5000/health
```

### Performance Monitoring
- Use New Relic, Datadog, or similar APM tools
- Monitor Python processes with `psutil`

### Error Tracking
- Integrate Sentry for error tracking
- Set up email alerts for critical errors

## Backup & Recovery

### Database Backups
(If using database in future)

### Code Backups
```bash
git backup --mirror /path/to/backup.git
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port
lsof -i :5000

# Kill process
kill -9 <PID>
```

### Memory Issues
- Increase server RAM
- Use `gunicorn` worker limits: `--max-requests 1000`

### Slow Requests
- Check AI categorization performance
- Cache results
- Implement request timeout limits

## Scaling

### Horizontal Scaling
- Use load balancer (Nginx, HAProxy)
- Deploy multiple instances
- Use sticky sessions for stateful operations

### Vertical Scaling
- Increase server resources (CPU, RAM)
- Optimize database queries
- Use caching strategies

---

For more help, see [README.md](README.md)
