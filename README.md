# HappyRobot Challenge - Inbound Carrier Sales

Automated inbound carrier call system for freight brokerage. Carriers call in to request loads, get vetted via FMCSA, receive load matches, and negotiate pricing — all handled by an AI voice agent.

## Live URLs

- **API:** https://happyrobot-challenge-production-c876.up.railway.app
- **Dashboard:** https://happyrobot-challenge-production-c876.up.railway.app/dashboard/dashboard.html
- **Health Check:** https://happyrobot-challenge-production-c876.up.railway.app/health
- **API Docs:** https://happyrobot-challenge-production-c876.up.railway.app/docs

## API Authentication

All endpoints require the header:
X-API-Key: hr-dev-key-2024
## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/carrier/verify | Verify carrier MC number via FMCSA |
| POST | /api/loads/search | Search loads by origin, destination, equipment |
| GET | /api/loads/ | List all available loads |
| POST | /api/loads/negotiate | Evaluate a carrier's counter offer |
| POST | /api/calls/ | Log a call |
| GET | /api/calls/ | List all calls |
| GET | /api/metrics/ | Dashboard metrics |

## How to Reproduce

### Prerequisites
- Python 3.11+
- Docker (optional)

### Local Setup
```bash
git clone https://github.com/AlvaroG88/happyrobot-challenge.git
cd happyrobot-challenge
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
DATABASE_URL=sqlite:///./happyrobot.db
API_KEY=hr-dev-key-2024
FMCSA_API_KEY=your_fmcsa_webkey
Seed the database and run:
```bash
python -m app.seed
uvicorn app.main:app --reload
```

### Docker
```bash
docker-compose up --build
```

### Deploy to Railway
1. Fork or push this repo to GitHub
2. Go to railway.app → New Project → Deploy from GitHub Repo
3. Select the repository
4. Add environment variables: `API_KEY`, `FMCSA_API_KEY`, `DATABASE_URL`
5. Go to Settings → Networking → Generate Domain
6. Railway auto-detects the Dockerfile and deploys with HTTPS

## Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Carrier Verification:** FMCSA QCMobile API
- **Dashboard:** HTML, Chart.js
- **Deployment:** Docker, Railway