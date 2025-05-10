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

#def autodownloader(num,query):
    #pag.moveTo(110, 125, duration=.2)
    #pag.click(110, 125)
    #pag.typewrite(f'{query}')
    #pag.typewrite(['enter'])
    #pag.moveTo(80, 275, duration=.2)
    
    #i = 0
    #while i < num:
        #print(f'Iteration number: {i}')
        #time.sleep(1)
        #pag.click(80,275)
        #time.sleep(1)
        #pag.click(825,375)
        #time.sleep(65)
        #pag.click(300,155)
        #time.sleep(1)
        #pag.click(300,200)
        #time.sleep(1)
        #pag.click(300,30,button='middle')
        #pag.moveTo(80,275)
        #pag.scroll(random.randint(-245,-215))
        #time.sleep(1)
        #i += 1
        #iteration = (i/num) *100
        #if i < num:
            #print(f'You are {iteration}% done. Iteration number: {i} starting now.')
        #elif i >= num:
            #print(f'You are {iteration}% done.')
    
    #time.sleep(5)
    #pag.click(110, 125, clicks=3)
    #pag.typewrite(['backspace'])

#def renamer(num):
    #i = 0
    #pag.click(220,180)
    #while i < num:
        #name = i + 1
        #pag.typewrite(['F2'])
        #pag.typewrite(str(name))
        #pag.typewrite(['enter'])
        #time.sleep(1)
        #pag.typewrite(['down'])
        #i += 1

