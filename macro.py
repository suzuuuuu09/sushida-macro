import pyautogui as pg
import webbrowser
import auto_type
import sys
from time import sleep
 
try:
    args = sys.argv[1]
    if args not in ["e", "n", "h"]:
        print("\033[31mInvalid command line arguments.\ne: easy mode, n: normal mode, h: hard mode\033[39m")
        sys.exit()
except IndexError as e:
    print("\033[31mSet command line arguments.\ne: easy mode, n: normal mode, h: hard mode\033[39m")
    sys.exit()

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

if args == "e":
    location_course = pg.locateOnScreen("img/easy.png", confidence=0.9)
elif args == "n":
    location_course = pg.locateOnScreen("img/normal.png", confidence=0.9)
elif args == "h":
    location_course = pg.locateOnScreen("img/hard.png", confidence=0.9)
pg.moveTo(location_course)
sleep(0.05)
pg.click()
sleep(0.5)
pg.press("space")
sleep(2.5)
print("Press Enter to stop.")
auto_type.typing(args)