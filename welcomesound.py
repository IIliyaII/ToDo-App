
import os
import sys
import pygame


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def welcomesound():
    pygame.mixer.init()

    file_path = resource_path("femalewelcome.mp3")

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def byesound():
    pygame.mixer.init()

    file_path = resource_path("femalegoodbye.mp3")

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)