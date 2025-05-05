## orchestration/scheduler.py
from utils.logger import log_event

def add_task(task_type: str, payload: str):
    log_event(f"Task scheduled: {task_type} with payload: {payload}")
    return {"queued": True, "type": task_type, "payload": payload}
