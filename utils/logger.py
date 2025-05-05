## utils/logger.py
import logging
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)
log_filename = f"logs/carolina_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def log_event(event):
    print(f"[LOG]: {event}")
    logging.info(event)
