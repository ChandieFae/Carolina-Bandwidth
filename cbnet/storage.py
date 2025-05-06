## cbnet/storage.py
"""
CBNet Storage Module

Provides persistent storage for queued jobs and results.
Uses local JSON files as a simple database.
"""

import os
import json
from typing import List
from cbnet.agent import CBJob, CBResult

DATA_DIR = "cbnet/storage"
JOBS_FILE = os.path.join(DATA_DIR, "jobs.json")
RESULTS_FILE = os.path.join(DATA_DIR, "results.json")

os.makedirs(DATA_DIR, exist_ok=True)

def load_jobs() -> List[CBJob]:
    if not os.path.exists(JOBS_FILE):
        return []
    with open(JOBS_FILE, "r") as f:
        raw = json.load(f)
    return [CBJob(**job) for job in raw]

def save_jobs(jobs: List[CBJob]):
    with open(JOBS_FILE, "w") as f:
        json.dump([job.__dict__ for job in jobs], f, indent=2)

def load_results() -> List[CBResult]:
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as f:
        raw = json.load(f)
    return [CBResult(**r) for r in raw]

def save_results(results: List[CBResult]):
    with open(RESULTS_FILE, "w") as f:
        json.dump([r.__dict__ for r in results], f, indent=2)


## cbnet/agent.py (updated)
...
from cbnet import storage  # add this
...
class CBAgent:
    def __init__(self):
        self.queue = CBQueue()
        self.results = storage.load_results()
        for job in storage.load_jobs():
            self.queue.add(job)

    def handle_job(self, job: CBJob):
        print(f"Executing job {job.id} of type '{job.type}'")
        result = {"status": "success", "echo": job.payload}
        cb_result = CBResult(job.id, result)
        self.results.append(cb_result)
        storage.save_results(self.results)
        return result

    def queue_job(self, job_type: str, payload: dict):
        job = CBJob(job_type, payload)
        self.queue.add(job)
        jobs = [job]
        while not self.queue.q.empty():
            jobs.append(self.queue.q.get())
        for j in jobs[1:]:
            self.queue.q.put(j)
        storage.save_jobs(jobs)
        return job.id

    def run_queue(self):
        jobs = []
        while True:
            job = self.queue.next()
            if not job:
                break
            jobs.append(job)
            self.handle_job(job)
        storage.save_jobs([])  # Clear queue after running

    def get_results(self):
        return [r.__dict__ for r in self.results]
