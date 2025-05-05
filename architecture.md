# docs/architecture.md
# Carolina Bandwidth – Architecture

This document describes the core architecture of the Carolina Bandwidth platform.

## Components
- **API** – FastAPI-based REST endpoints
- **Frontend** – Streamlit dashboard
- **Model Layer** – Pluggable modules for text, audio, image
- **Scheduler** – Task orchestration via Python
- **Pipelines** – Ingestion and processing logic

## Data Flow
```
[Ingestion] -> [Pipeline] -> [Model] -> [Results API + Dashboard]
```
