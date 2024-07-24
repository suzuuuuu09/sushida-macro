import image
import pyautogui
import keyboard
from time import sleep

def typing():
    for i in range(360):
        path = "img/screenshot.png"
        pyautogui.screenshot(path, region = (855, 420, 330, 30))
        text = image.transcription(path)
        pyautogui.typewrite(text)
        sleep(0.1)
        if keyboard.is_pressed("enter"):
            break