# Context-Aware Voice Dictation Engine

A local-first, low-latency voice dictation system that runs entirely on your machine. Hold F8, speak naturally, and inject formatted text directly at your cursor position—perfect for coding, writing emails, taking notes, or general dictation.

## ✨ Features

- **🎯 Context-Aware Formatting**: Automatically formats your speech based on the current context
  - `programming`: Code-focused output with keyword recognition
  - `plain`: Standard dictation with proper capitalization
  - `email`: Professional email templates with greetings and signatures
  - `notes`: Bullet-point formatting for quick note-taking

- **⚡ Low Latency**: Local processing means no cloud delays—typically under 2 seconds from speech to text
- **🔒 Privacy-First**: All audio processing happens on your machine; nothing is sent to external servers
- **⌨️ Keyboard-Driven**: Simple F8 hold-to-record interface that works system-wide
- **🎤 Smart Audio Processing**: Automatic silence trimming and normalization for better transcription accuracy
- **📋 Seamless Integration**: Injects text directly at your cursor position without disrupting your workflow

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Windows OS (for `pyautogui` keyboard injection)
- Microphone

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/context-aware-voice-dictation-engine.git
cd context-aware-voice-dictation
```

2. Install dependencies:
```bash
pip install pynput sounddevice soundfile numpy pyperclip pyautogui faster-whisper
```

3. Run the application:
```bash
python app.py
```

### Usage

1. Launch the application—you'll see: `Hold F8 to speak. Ctrl+C to exit.`
2. Click into any text field or code editor
3. Hold **F8** and speak naturally
4. Release **F8** when finished
5. Your formatted text appears at the cursor automatically

**Example (Programming Context):**
- Speak: *"define a function is prime open parenthesis n close parenthesis colon"*
- Output: `def is_prime(n):`

## 📁 Project Structure

```
├── app.py                    # Main entry point & keyboard listener
├── audio_input.py           # Real-time audio capture with threading
├── audio_preprocessing.py   # Silence trimming & normalization
├── stt.py                   # Speech-to-text using Whisper
├── formatter.py             # Context-aware text formatting
└── injector.py              # Clipboard-based text injection
```

## 🎛️ Configuration

### Change Context Mode

Edit `CONTEXT` in `app.py`:

```python
CONTEXT = "programming"  # Options: "plain", "programming", "email", "notes"
```

### Adjust Audio Settings

In `audio_input.py`:
```python
SAMPLE_RATE = 16000  # Audio sample rate
CHANNELS = 1         # Mono audio
```

### Modify Hotkey

In `app.py`, change `keyboard.Key.f8` to any other key:
```python
if key == keyboard.Key.f9 and not pressed:  # Use F9 instead
```

## 🔧 How It Works

1. **Audio Capture**: `audio_input.py` continuously streams audio from your microphone using `sounddevice`
2. **Recording Control**: Pressing F8 triggers buffering; releasing F8 stops and saves to `input.wav`
3. **Preprocessing**: `audio_preprocessing.py` removes silence and normalizes volume for better transcription
4. **Transcription**: `stt.py` uses Whisper (small.en model) to convert speech to text
5. **Formatting**: `formatter.py` applies context-specific rules (e.g., "colon" → `:` in programming mode)
6. **Injection**: `injector.py` uses clipboard manipulation and Ctrl+V to paste at the cursor

## 🎨 Formatting Examples

### Plain Mode
- Input: *"hello world period how are you"*
- Output: `Hello world. How are you`

### Programming Mode
- Input: *"define a function calculate open parenthesis x comma y close parenthesis colon new line"*
- Output: `def calculate(x, y):\n`

### Email Mode
- Input: *"I would like to schedule a meeting next week"*
- Output:
```
Dear Sir/Madam,

I would like to schedule a meeting next week

Thank you for your understanding.

Regards,
```

### Notes Mode
- Input: *"first buy groceries second call dentist third finish report"*
- Output:
```
- Buy groceries
- Call dentist
- Finish report
```

## 🛠️ Troubleshooting

**No audio being recorded:**
- Check microphone permissions in Windows settings
- Verify your default recording device is correct
- Test microphone with: `python -m sounddevice`

**Transcription is inaccurate:**
- Speak more clearly and at a moderate pace
- Ensure you're in a quiet environment
- Adjust the silence threshold in `audio_preprocessing.py` (line 29)

**Text not injecting:**
- Ensure the target application accepts Ctrl+V paste commands
- Check that `pyautogui` has permission to control keyboard input
- Try increasing sleep delays in `injector.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Faster Whisper**: Fast and efficient speech recognition
- **OpenAI Whisper**: The underlying model powering transcription
- **pynput**: Cross-platform keyboard control library

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for developers who code faster by speaking**
