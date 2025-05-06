import pyautogui as pag
import time
import random

print(pag.size())

#pag.moveTo(110,125)
#pag.moveTo(80,275)
#pag.moveTo(770,375)
#pag.moveTo(300,155)
#pag.moveTo(300,30)
#pag.scroll(random.randint(-245,-215))

def autodownloader(num,query):
    pag.moveTo(110, 125, duration=.2)
    pag.click(110, 125)
    pag.typewrite(f'{query}')
    pag.typewrite(['enter'])
    pag.moveTo(80, 275, duration=.2)
    
    i = 0
    while i < num:
        time.sleep(1)
        pag.click(80,275)
        time.sleep(1)
        pag.click(825,375)
        time.sleep(65)
        pag.click(300,155)
        time.sleep(1)
        pag.click(300,200)
        time.sleep(1)
        pag.click(300,30,button='middle')
        pag.moveTo(80,275)
        pag.scroll(random.randint(-245,-215))
        i += 1
    
    time.sleep(5)
    pag.click(110, 125, clicks=3)
    pag.typewrite(['backspace'])

autodownloader(2,'Hospitals in West Virginia')