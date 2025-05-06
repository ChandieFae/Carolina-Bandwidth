## cbnet/orchestrator.py
"""
CBNet Orchestrator API

Provides HTTP endpoints to submit jobs to the CBNet Agent and retrieve results.
This is the central hub coordinating jobs from distributed edge agents.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cbnet.agent import CBAgent, CBJob

app = FastAPI(title="CBNet Orchestrator")
agent = CBAgent()

class JobRequest(BaseModel):
    job_type: str
    payload: dict

@app.get("/")
def root():
    return {"message": "CBNet Orchestrator is live."}

@app.post("/submit")
def submit_job(req: JobRequest):
    job_id = agent.queue_job(req.job_type, req.payload)
    return {"job_id": job_id, "status": "queued"}

@app.get("/run")
def run_jobs():
    agent.run_queue()
    return {"status": "completed"}

@app.get("/results")
def get_results():
    return {"results": agent.get_results()}
