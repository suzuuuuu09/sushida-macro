import image
import pyautogui
from time import sleep

def typing():
    for i in range(200):
        path = "screenshot.png"
        pyautogui.screenshot(path, region = (810, 420, 370, 30))
        text = image.transcription(path)
        pyautogui.typewrite(text)
        sleep(0.1)