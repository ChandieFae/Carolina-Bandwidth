## CHECKLIST.md
# ✅ Carolina Bandwidth — Project Checklist

## 🔧 Core System
- [✅] FastAPI backend (`api/main.py`)
- [✅] Streamlit frontend (`frontend/app.py`)
- [✅] Model stubs (GPT + Whisper)
- [✅] Data pipelines (ingestion + processing)
- [✅] Job queue scheduler (`orchestration/`)
- [✅] Dockerfile + docker-compose setup
- [✅] GitHub Actions CI
- [✅] `tests/` folder with FastAPI test
- [✅] `experiments/` benchmark file
- [✅] `docs/` with architecture, setup, roadmap

## 🧪 Local Dev / Testing
- [ ] Run `uvicorn api.main:app --reload`
- [ ] Run `streamlit run frontend/app.py`
- [ ] Run `pytest tests/`
- [ ] Run `docker-compose up --build`
- [ ] Trigger `/text` and `/audio` endpoints with test inputs

## 🚀 Feature Expansion (Optional Next Steps)
- [ ] Replace `run_gpt()` with real GPT API or local LLM
- [ ] Replace `transcribe_audio()` with real Whisper model
- [ ] Build frontend job queue visualization (Streamlit)
- [ ] Add persistent storage (SQLite, JSON, or S3)
- [ ] Add background job queue (Celery / RQ / Ray)
- [ ] Add logging to file with timestamps
- [ ] Add `.env` config loading
- [ ] Add metrics endpoint for Prometheus
- [ ] Add GPU/CPU system monitoring (Grafana)
- [ ] Add vector DB support (e.g., FAISS, LanceDB, Chroma)
- [ ] Integrate job queue UI with `st.dataframe()` in Streamlit
- [ ] Add `requirements.txt` or `pyproject.toml` for full dependency control

## 🌍 Deployment
- [ ] Deploy API on Render, Fly.io, or HuggingFace Spaces
- [ ] Serve dashboard publicly
- [ ] Add CORS + security headers to API
- [ ] Add `/health` or `/status` endpoint
