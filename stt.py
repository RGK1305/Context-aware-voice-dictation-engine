from faster_whisper import WhisperModel

model = WhisperModel("small.en", device="cpu", compute_type="int8")

def transcribe(path):
    segments, _ = model.transcribe(path, language="en")
    return " ".join(segment.text.strip() for segment in segments)
