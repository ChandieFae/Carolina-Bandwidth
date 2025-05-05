## api/main.py
from fastapi import FastAPI
from models.gpt_runner import run_gpt
from models.whisper_loader import transcribe_audio
from orchestration.scheduler import add_task
from utils.logger import log_event
from vectorstore.vector_handler import add_to_vector_store, search_vector_store
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Carolina Bandwidth is live"}

@app.post("/text")
def process_text(input_text: str):
    log_event("Text processing requested")
    result = run_gpt(input_text)
    add_to_vector_store(input_text)
    return result

@app.post("/audio")
def process_audio(file_path: str):
    log_event("Audio transcription requested")
    return transcribe_audio(file_path)

@app.post("/queue-task")
def queue_task(task_type: str, payload: str):
    log_event(f"Queuing task: {task_type}")
    return add_task(task_type, payload)

@app.get("/search")
def search_vectors(query: str):
    return search_vector_store(query)
