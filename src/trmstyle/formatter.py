import random

from .colors import Color

def color(text, style):
    return f"{style}{text}{Color.RESET}"

def rainbow_words(text):
    words = text.split(" ")

    result = []

    for word in words:
        color = random.choice(Color.RAINBOW)
        result.append(f"{color}{word}{Color.RESET}")

    return " ".join(result)
