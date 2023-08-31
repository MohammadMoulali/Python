import random
import pyautogui as pg
import time
animal = ("monkey", "donkey", "pokkadi")
time.sleep(8)
for i in range(50):
    a = random.choice(animal)
    pg.write("you are monkey"+a)
    pg.press("enter")
