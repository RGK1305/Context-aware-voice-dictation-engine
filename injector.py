import pyperclip
import pyautogui
import time

def inject_text(text: str):
    # Save current clipboard
    old_clipboard = pyperclip.paste()

    try:
        # Copy new text
        pyperclip.copy(text)
        time.sleep(0.05)

        # Paste
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.05)

    finally:
        # Restore clipboard
        pyperclip.copy(old_clipboard)
