"""Morse code converter."""

import pygame
import time

pygame.mixer.init()

dash_sound = pygame.mixer.Sound("sounds/dash.wav")
dot_sound = pygame.mixer.Sound("sounds/dot.wav")

morris_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def convert_to_morse(text: str) -> str:
    """Converts text to morse code."""

    result = ""

    for letter in text:
        if letter == " ":
            result += " "
        elif letter not in morris_dict:
            print(f"Invalid character: {letter}")
            continue
        else:
            result += morris_dict[letter] + " "

    return result

def play_morse_code(morse_code: str) -> None:
    """PLays morse code."""
    for letter in morse_code:
        print(letter)
        if letter == ".":
            dot_sound.play()
            time.sleep(0.3)
        elif letter == "-":
            dash_sound.play()
            time.sleep(.6)
        else:
            time.sleep(.2)

if __name__ == "__main__":
    user_input = input("Enter a word to convert to morse code: ").lower()
    morse_code = convert_to_morse(user_input)
    play_morse_code(morse_code)