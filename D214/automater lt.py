import pyautogui as pag
import time
import random

print(pag.size())

def autodownloader(num,query):
    pag.moveTo(110, 155, duration=.2)
    pag.click(110, 155)
    pag.typewrite(f'{query}')
    pag.typewrite(['enter'])
    pag.moveTo(110, 350, duration=.2)
    
    i = 0
    while i < num:
        time.sleep(1)
        pag.click(110,350)
        time.sleep(1)
        pag.click(770,475)
        time.sleep(65)
        pag.click(300,200)
        time.sleep(1)
        pag.click(300,245)
        time.sleep(1)
        pag.click(400,30,button='middle')
        pag.click(75,30)
        pag.click(80,155)
        pag.moveTo(110,350)
        pag.scroll(random.randint(-245,-215))
        i += 1
    
    time.sleep(5)
    pag.click(110, 155, clicks=3)
    pag.typewrite(['backspace'])

autodownloader(2,'Hospitals in West Virginia')