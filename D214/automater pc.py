import pyautogui as pag
import time
import random

print(pag.size())

pag.moveTo(110,125)
pag.moveTo(80,275)
pag.moveTo(770,375)
pag.moveTo(300,155)
pag.moveTo(300,30)
pag.scroll(random.randint(-245,-215))

def autodownloader(num,query):
    pag.moveTo(110, 125, duration=.2)
    pag.click(110, 125)
    pag.typewrite(f'{query}')
    pag.typewrite(['enter'])
    pag.moveTo(80, 275, duration=.2)
    
    i = 0
    while i < num:
        print(f'Iteration number: {i}')
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
        time.sleep(1)
        i += 1
        iteration = (i/num) *100
        if i < num:
            print(f'You are {iteration}% done. Iteration number: {i} starting now.')
        elif i >= num:
            print(f'You are {iteration}% done.')
    
    time.sleep(5)
    pag.click(110, 125, clicks=3)
    pag.typewrite(['backspace'])

def renamer(num):
    i = 0
    pag.click(220,180)
    while i < num:
        name = i + 1
        pag.typewrite(['F2'])
        pag.typewrite(str(name))
        pag.typewrite(['enter'])
        time.sleep(1)
        pag.typewrite(['down'])
        i += 1

def df_creation(num):
    i = 0
    pag.click(300,250)
    while i < num:
        name = i + 1
        pag.typewrite(f'df{name} = pd.read_csv("{name}.csv")')
        pag.typewrite(['enter'])
        i += 1

def concat_auto(num):
    i = 0
    pag.click(453,482)
    while i < num:
        name = i + 1
        pag.typewrite(f'df{name}, ')
        i += 1
        if i == 20:
            pag.typewrite(['enter'])
        if i == 40:
            pag.typewrite(['enter'])
        if i == 60:
            pag.typewrite(['enter'])
        if i == 80:
            pag.typewrite(['enter'])
        if i == 100:
            pag.typewrite(['enter'])
        if i == 120:
            pag.typewrite(['enter'])
        if i == 140:
            pag.typewrite(['enter'])
        if i == 160:
            pag.typewrite(['enter'])
        if i == 180:
            pag.typewrite(['enter'])
        if i == 200:
            pag.typewrite(['enter'])
        if i == 220:
            pag.typewrite(['enter'])
        if i == 240:
            pag.typewrite(['enter'])
        if i == 260:
            pag.typewrite(['enter'])
        if i == 280:
            pag.typewrite(['enter'])
        if i == 300:
            pag.typewrite(['enter'])
        if i == 320:
            pag.typewrite(['enter'])
        if i == 340:
            pag.typewrite(['enter'])
        if i == 360:
            pag.typewrite(['enter'])
        if i == 380:
            pag.typewrite(['enter'])
        if i == 400:
            pag.typewrite(['enter'])
        if i == 420:
            pag.typewrite(['enter'])
        if i == 440:
            pag.typewrite(['enter'])
        if i == 460:
            pag.typewrite(['enter'])
        if i == 480:
            pag.typewrite(['enter'])
        if i == 500:
            pag.typewrite(['enter'])
        if i == 520:
            pag.typewrite(['enter'])
        if i == 540:
            pag.typewrite(['enter'])
        if i == 560:
            pag.typewrite(['enter'])
        if i == 580:
            pag.typewrite(['enter'])
        if i == 600:
            pag.typewrite(['enter'])
        if i == 620:
            pag.typewrite(['enter'])
        if i == 640:
            pag.typewrite(['enter'])
        if i == 660:
            pag.typewrite(['enter'])
        if i == 680:
            pag.typewrite(['enter'])
        if i == 700:
            pag.typewrite(['enter'])
        if i == 720:
            pag.typewrite(['enter'])
        if i == 740:
            pag.typewrite(['enter'])
        if i == 760:
            pag.typewrite(['enter'])
        if i == 780:
            pag.typewrite(['enter'])
        if i == 800:
            pag.typewrite(['enter'])
        if i == 820:
            pag.typewrite(['enter'])
        if i == 840:
            pag.typewrite(['enter'])
        if i == 860:
            pag.typewrite(['enter'])
        if i == 880:
            pag.typewrite(['enter'])
        if i == 900:
            pag.typewrite(['enter'])
        if i == 920:
            pag.typewrite(['enter'])
        if i == 940:
            pag.typewrite(['enter'])
        if i == 960:
            pag.typewrite(['enter'])
        if i == 980:
            pag.typewrite(['enter'])
        if i == 1000:
            pag.typewrite(['enter'])
        if i == 1020:
            pag.typewrite(['enter'])
        if i == 1040:
            pag.typewrite(['enter'])
        if i == 1060:
            pag.typewrite(['enter'])
        if i == 1080:
            pag.typewrite(['enter'])
        if i == 1100:
            pag.typewrite(['enter'])
        if i == 1120:
            pag.typewrite(['enter'])
        if i == 1140:
            pag.typewrite(['enter'])
        if i == 1160:
            pag.typewrite(['enter'])
        if i == 1180:
            pag.typewrite(['enter'])
        if i == 1200:
            pag.typewrite(['enter'])
        if i == 1220:
            pag.typewrite(['enter'])
        if i == 1240:
            pag.typewrite(['enter'])
        if i == 1260:
            pag.typewrite(['enter'])
        if i == 1280:
            pag.typewrite(['enter'])
        if i == 1300:
            pag.typewrite(['enter'])
        if i == 1320:
            pag.typewrite(['enter'])
        if i == 1340:
            pag.typewrite(['enter'])
        if i == 1360:
            pag.typewrite(['enter'])
        if i == 1380:
            pag.typewrite(['enter'])
        if i == 1400:
            pag.typewrite(['enter'])
        if i == 1420:
            pag.typewrite(['enter'])
        if i == 1440:
            pag.typewrite(['enter'])

def concat_auto_2(num):
    i = 1521
    pag.click(300,155)
    while i < num:
        name = i + 1
        pag.typewrite(f'df{name}, ')
        i += 1
        if i == 1540:
            pag.typewrite(['enter'])
        if i == 1560:
            pag.typewrite(['enter'])
        if i == 1580:
            pag.typewrite(['enter'])

def df_creation2(num):
    i = 1521
    pag.click(300,155)
    while i < num:
        name = i + 1
        pag.typewrite(f'df{name} = pd.read_csv("{name}.csv")')
        pag.typewrite(['enter'])
        i += 1

concat_auto_2(1591)