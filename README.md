# HappyRobot Challenge - Inbound Carrier Sales

Automated inbound carrier call system for freight brokerage. Carriers call in to request loads, get vetted via FMCSA, receive load matches, and negotiate pricing — all handled by an AI voice agent.

## Live URLs

- **Dashboard:** https://happyrobot-challenge-production-c876.up.railway.app/dashboard/dashboard.html
- **Health Check:** https://happyrobot-challenge-production-c876.up.railway.app/health
- **API Docs:** https://happyrobot-challenge-production-c876.up.railway.app/docs

## API Authentication

All endpoints require the header:
X-API-Key: hr-dev-key-2024
## API Endpoints
 
| Method | Endpoint               | Description                         |
|--------|------------------------|-------------------------------------|
| POST   | /api/carrier/verify    | Verify carrier MC number via FMCSA  |
| POST   | /api/loads/search      | Search loads by filters             |
| POST   | /api/loads/negotiate   | Evaluate carrier counter offer      |
| POST   | /api/calls/            | Log a call                          |
| GET    | /api/loads/            | List all loads                      |
| GET    | /api/calls/            | List all calls                      |
| GET    | /api/metrics/          | Dashboard metrics                   |
| GET    | /api/metrics/top-lanes | Top lanes by volume                 |
 

## How to Reproduce

### Prerequisites
- Python 3.11+
- Docker (optional)

## Quick Start
 
### Docker (one command)
```bash
git clone https://github.com/AlvaroG88/happyrobot-challenge.git
cd happyrobot-challenge
# Create .env with: DATABASE_URL, API_KEY, FMCSA_API_KEY
docker-compose up --build
```
 
### Local
```bash
git clone https://github.com/AlvaroG88/happyrobot-challenge.git
cd happyrobot-challenge
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```
 
Create `.env`:
```
DATABASE_URL=sqlite:///./happyrobot.db
API_KEY=hr-dev-key-2024
FMCSA_API_KEY=your_fmcsa_webkey
```
 
```bash
python -m app.seed
uvicorn app.main:app --reload
```
 
### Deploy to Railway
1. Push repo to GitHub
2. Railway → New Project → Deploy from GitHub Repo
3. Add environment variables: `API_KEY`, `FMCSA_API_KEY`, `DATABASE_URL`
4. Settings → Networking → Generate Domain
5. HTTPS is automatic

## Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Carrier Verification:** FMCSA QCMobile API
- **Dashboard:** HTML, Chart.js
- **Deployment:** Docker, Railway