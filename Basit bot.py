from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui as pg
# 689-518
url="https://www.youtube.com/watch?v=D6dmO7mqOfU"
browser=webdriver.Firefox()
sleep(3)
browser.maximize_window()
sleep(3)
browser.get(url)
sleep(3)
konum=pg.moveTo(689,518)
sleep(3)
pg.click(689,518)
sleep(3)
browser.close()




