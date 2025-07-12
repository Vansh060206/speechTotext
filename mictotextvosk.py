import sounddevice as sd
import queue
import vosk
import sys
import json

model_path = "vosk-model-small-en-us-0.15"

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def recognize_from_mic_vosk():
    model = vosk.Model(model_path)
    samplerate = 16000

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Say something (Ctrl+C to stop)...")

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                print("You said:", result.get("text", ""))

if __name__ == "__main__":
    recognize_from_mic_vosk()
