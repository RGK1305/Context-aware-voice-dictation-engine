import sounddevice as sd
import soundfile as sf
import numpy as np
import threading

SAMPLE_RATE = 16000
CHANNELS = 1

recording = []
is_recording = False
lock = threading.Lock()

def audio_callback(indata, frames, time, status):
    global recording, is_recording
    if is_recording:
        with lock:
            recording.append(indata.copy())

stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    callback=audio_callback
)

stream.start()

def start_recording():
    global is_recording, recording
    if is_recording:
        return
    with lock:
        recording = []
        is_recording = True

def stop_recording():
    global is_recording, recording
    if not is_recording:
        return
    with lock:
        is_recording = False
        if not recording:
            return
        audio = np.concatenate(recording, axis=0)
    sf.write("input.wav", audio, SAMPLE_RATE)
