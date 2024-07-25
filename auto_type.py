import pyautogui as pg
import numpy as np
import image
import keyboard
import cv2
from time import sleep

def typing(mode: str):
    location = image.find_image_on_screen("img/menu.png")
    x, y, scale = location[0], location[1], location[4]
    for i in range(360):
        path = "img/text.png"
        r, w = 0, 0
        if mode == "e":
            r, w = x + 179 * scale, 150 * scale
        elif mode == "n":
            r, w = x + 128 * scale, 250 * scale
        elif mode == "h":
            r, w = x + 77 * scale, 345 * scale
        pg.screenshot(path, region = (r, y - 155 * scale, w, 30 * scale))
        text = image.transcription(path)
        pg.typewrite(text)
        print(f"{text}", end="")
        sleep(0.1)
        if keyboard.is_pressed("enter"):
            break