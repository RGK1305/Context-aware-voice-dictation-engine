from pynput import keyboard
from audio_input import start_recording, stop_recording
from audio_preprocessing import process_audio
from stt import transcribe
from formatter import format_text
from injector import inject_text

CONTEXT = "programming"
pressed = False

def on_press(key):
    global pressed
    if key == keyboard.Key.f8 and not pressed:
        pressed = True
        start_recording()
        print("🎤 Recording started")

def on_release(key):
    global pressed
    if key == keyboard.Key.f8 and pressed:
        pressed = False
        stop_recording()
        process_audio()
        raw = transcribe("clean.wav")
        final = format_text(raw, CONTEXT)
        inject_text(final)
        print("✅ Text injected")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Hold F8 to speak. Ctrl+C to exit.")
    listener.join()
