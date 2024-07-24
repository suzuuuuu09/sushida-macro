import image
import pyautogui as pg
import keyboard
from time import sleep

def typing():
    for i in range(360):
        location = pg.locateOnScreen("img/shoyu.png", confidence=0.8)
        center_x, center_y = location[0], location[1] + location[3] / 2
        path = "img/text.png"
        pg.screenshot(path, region = (center_x + 30, center_y - 123, 345, 30))
        text = image.transcription(path)
        pg.typewrite(text)
        print(f"{text}", end="")
        sleep(0.1)
        if keyboard.is_pressed("enter"):
            break