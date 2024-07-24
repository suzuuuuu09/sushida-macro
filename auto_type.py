import image
import pyautogui
from time import sleep

def typing():
    for i in range(360):
        path = "img/screenshot.png"
        pyautogui.screenshot(path, region = (855, 420, 330, 30))
        text = image.transcription(path)
        pyautogui.typewrite(text)
        sleep(0.1)