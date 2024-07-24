import pyautogui as pg
import numpy as np
import image
import keyboard
import cv2
from time import sleep

def typing():
    location = image.find_image_on_screen("img/menu.png")
    x, y, scale = location[0], location[1], location[4]
    print(x, y)
    for i in range(360):
        path = "img/text.png"
        pg.screenshot(path, region = ((x + 77 * scale), y - 155 * scale, 345 * scale, 30 * scale))
        text = image.transcription(path)
        pg.typewrite(text)
        print(f"{text}", end="")
        sleep(0.1)
        if keyboard.is_pressed("enter"):
            break
