CONTEXTS = {
    "plain": "Plain dictation",
    "programming": "Code-focused output",
    "email": "Professional email writing",
    "notes": "Bullet-point notes"
}

import re

def base_cleanup(text: str) -> str:
    text = text.strip()

    # Normalize spaces
    text = re.sub(r"\s+", " ", text)

    # Fix common verbal tokens
    replacements = {
        "comma": ",",
        "period": ".",
        "full stop": ".",
        "new line": "\n",
        "colon": ":",
        "semicolon": ";",
    }

    for k, v in replacements.items():
        text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

    return text

def format_plain(text: str) -> str:
    text = base_cleanup(text)

    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]

    return text

def format_notes(text: str) -> str:
    text = base_cleanup(text)

    # Split on common sequencing words
    parts = re.split(
        r"\b(first|second|third|next|finally)\b",
        text,
        flags=re.IGNORECASE
    )

    bullets = []
    for p in parts:
        p = p.strip()
        if len(p) > 2:
            bullets.append("- " + p.capitalize())

    return "\n".join(bullets)

def format_email(text: str) -> str:
    text = base_cleanup(text)

    body = text[0].upper() + text[1:]

    return (
        "Dear Sir/Madam,\n\n"
        f"{body}\n\n"
        "Thank you for your understanding.\n\n"
        "Regards,\n"
    )

def is_prime(n):
    return True

def format_programming(text: str) -> str:
    text = base_cleanup(text)

    # Structural keywords — ONLY when explicit
    structure_map = {
        "define a function": "def",
        "create function": "def",
        "define class": "class",
        "create class": "class",
    }

    symbol_map = {
        "open parenthesis": "(",
        "close parenthesis": ")",
        "colon": ":",
        "new line": "\n",
        "equals": "=",
        "double equals": "==",
    }

    for k, v in structure_map.items():
        text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

    for k, v in symbol_map.items():
        text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

    return text




def format_text(text: str, context: str) -> str:
    if context == "plain":
        return format_plain(text)
    if context == "notes":
        return format_notes(text)
    if context == "email":
        return format_email(text)
    if context == "programming":
        return format_programming(text)

    return text
