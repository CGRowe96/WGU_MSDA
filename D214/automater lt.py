import pyautogui as pag
import time
import random

print(pag.size())

def autodownloader(num,query):
    time.sleep(1)
    pag.moveTo(110, 155, duration=.2)
    pag.click(110, 155)
    time.sleep(1)
    pag.typewrite(f'{query}')
    pag.typewrite(['enter'])
    pag.moveTo(110, 350, duration=.2)
    
    i = 0
    while i < num:
        print(f'Iteration number: {i}')
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
        time.sleep(2)
        pag.click(75,30)
        time.sleep(2)
        pag.click(80,155)
        time.sleep(2)
        pag.moveTo(110,350)
        time.sleep(2)
        pag.scroll(random.randint(-245,-215))
        time.sleep(2)
        i += 1
        iteration = (i/num) *100
        if i < num:
            print(f'You are {iteration}% done. Iteration number: {i} starting now.')
        elif i >= num:
            print(f'You are {iteration}% done.')
    
    time.sleep(5)
    pag.click(110, 155, clicks=3)
    pag.typewrite(['backspace'])

autodownloader(2,'Hospitals in West Virginia')