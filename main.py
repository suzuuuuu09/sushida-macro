import pyautogui as pg
import webbrowser
import auto_type
import sys
from time import sleep
from choice_selector import ChoiceSelector
from terminal import Terminal

options = ["easy", "normal", "hard"]

terminal = Terminal()
selector = ChoiceSelector(options, 1)

terminal.clear_screen()
select = selector.run()

url = 'https://sushida.net'
webbrowser.open(url, new=2, autoraise=True)
sleep(2)
pg.click("img/play.png")
sleep(4)

location_start = pg.locateOnScreen("img/start.png", confidence=0.7)
pg.moveTo(location_start)
sleep(0.05)
pg.click()
sleep(2)

location_course = pg.locateOnScreen(f"img/{select}.png", confidence=0.9)

pg.moveTo(location_course)
sleep(0.05)
pg.click()
sleep(0.5)
pg.press("space")
sleep(2.5)
print("Press Enter to stop.")
auto_type.typing(select)