## models/whisper_loader.py
import whisper
import os

model = whisper.load_model("base")

def transcribe_audio(file_path: str):
    try:
        result = model.transcribe(file_path)
        return {"transcript": result["text"]}
    except Exception as e:
        return {"error": str(e)}
