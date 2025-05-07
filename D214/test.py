import pyautogui as pag
import time
import random

#pag.moveTo(300,200)

def iteration_test(num):
    i = 0
    while i < num:
        print(f'Iteration number: {i}')
        time.sleep(2)
        print(random.randint(0,255))
        time.sleep(2)
        i += 1
        iteration = (i/num) *100
        if i < num:
            print(f'You are {iteration}% done. Iteration number: {i} starting now.')
        elif i >= num:
            print(f'You are {iteration}% done.')
            
iteration_test(6)