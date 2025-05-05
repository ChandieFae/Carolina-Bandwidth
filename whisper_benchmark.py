## experiments/whisper_benchmark.py
from time import time
from models.whisper_loader import transcribe_audio

start = time()
result = transcribe_audio("sample.wav")
end = time()
print("Result:", result)
print("Time taken:", end - start)
