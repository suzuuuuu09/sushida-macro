import pyautogui as pag
import webbrowser
import auto_type
from time import sleep
 
url = 'https://sushida.net'
webbrowser.open(url, new=2, autoraise=True)

sleep(2)
pag.click("img/play.png")

sleep(4)
location_start = pag.locateOnScreen("img/start.png", confidence=0.7)
pag.moveTo(location_start)
sleep(0.05)
pag.click()

sleep(0.5)
location_course = pag.locateOnScreen("img/course.png", confidence=0.9)
pag.moveTo(location_course)
sleep(0.05)
pag.click()

sleep(0.5)
pag.press("space")
sleep(0.5)

print("Press Enter to stop.")
auto_type.typing()