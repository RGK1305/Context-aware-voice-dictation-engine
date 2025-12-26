import numpy as np
import soundfile as sf


def process_audio():
    audio, sr = sf.read("input.wav")
    # load input.wav
    # trim silence
    # normalize
    # save clean.wav
    print("Sample rate:", sr)
    print("Shape:", audio.shape)
    if audio.ndim > 1:
        audio = audio[:, 0]
    def rms_energy(signal, frame_size=1024):
        energy = []
        for i in range(0, len(signal), frame_size):
            frame = signal[i:i+frame_size]
            rms = np.sqrt(np.mean(frame**2))
            energy.append(rms)
        return np.array(energy)
    def trim_silence(signal, threshold=0.01, frame_size=1024):
        energy = rms_energy(signal, frame_size)

        indices = np.where(energy > threshold)[0]

        if len(indices) == 0:
            return signal  # nothing detected

        start = indices[0] * frame_size
        end = indices[-1] * frame_size

        return signal[start:end]

    def normalize(signal, target_peak=0.9):
        peak = np.max(np.abs(signal))
        if peak == 0:
            return signal
        return signal * (target_peak / peak)

    audio, sr = sf.read("input.wav")

    if audio.ndim > 1:
        audio = audio[:, 0]

    audio = trim_silence(audio)
    audio = normalize(audio)

    sf.write("clean.wav", audio, sr)

    print("✅ Saved clean.wav")

    """import matplotlib.pyplot as plt

    plt.plot(audio)
    plt.title("Cleaned Audio Waveform")
    plt.show()"""
    pass

