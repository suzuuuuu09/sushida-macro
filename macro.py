import pyautogui
import webbrowser
import auto_type
from time import sleep
 
url = 'https://sushida.net'
webbrowser.open(url, new=2, autoraise=True)

sleep(2)
pyautogui.moveTo(1150, 530)
sleep(0.5)
pyautogui.click()
sleep(4)
pyautogui.moveTo(1000, 450)
sleep(0.5)
pyautogui.click()
sleep(0.5)
pyautogui.moveTo(1000, 520)
sleep(0.5)
pyautogui.click()
sleep(0.5)
pyautogui.press("space")
sleep(0.5)

auto_type.typing()