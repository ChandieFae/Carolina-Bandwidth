## docs/contributing.md
#Chandra Brown
# Contributing to Carolina Bandwidth

Thanks for wanting to contribute! Here's how to get started:

1. Fork the repo
2. Clone locally and set up the environment
3. Make changes in a branch
4. Run tests with `pytest`
5. Submit a PR with a clear description

We follow PEP8 + Black formatting, and aim for clean, modular code.


## docs/setup.md
# Setup Instructions

## Local Dev
```bash
git clone https://github.com/ChandieFae/Carolina-Bandwidth.git
cd Carolina-Bandwidth
pip install -r requirements.txt
uvicorn api.main:app --reload
```

## With Docker
```bash
docker-compose -f deployment/docker-compose.yml up --build
```

Visit the frontend: `streamlit run frontend/app.py`
