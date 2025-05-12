import pyautogui as pag
import time
import random

#pag.moveTo(550,200)
#pag.scroll(random.randint(-245,-215))

#def iteration_test(num):
    #i = 0
    
    #while i < num:
        #iteration = (i/num) *100
        #print(f'Iteration number: {i}')
        #if i < num:
            #print(f'You are {iteration}% done. Iteration number: {i} starting now.')
        #if i == (num/2):
            #print("Hello World!")
        #if i >= num:
            #print(f'You are {iteration}% done.')
        #time.sleep(2)
        #print(random.randint(0,255))
        #time.sleep(2)
        #i += 1
        
#iteration_test(6)

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

pag.moveTo(110,125)
pag.moveTo(80,275)