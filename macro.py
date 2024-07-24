import pyautogui as pg
import webbrowser
import auto_type
from time import sleep
 
url = 'https://sushida.net'
webbrowser.open(url, new=2, autoraise=True)

sleep(2)
pg.click("img/play.png")


sleep(4)
location_start = pg.locateOnScreen("img/start.png", confidence=0.7)
pg.moveTo(location_start)
sleep(0.05)
pg.click()

sleep(0.5)
location_course = pg.locateOnScreen("img/course.png", confidence=0.9)
pg.moveTo(location_course)
sleep(0.05)
pg.click()

sleep(0.5)
pg.press("space")
sleep(2.5)

print("Press Enter to stop.")
auto_type.typing()