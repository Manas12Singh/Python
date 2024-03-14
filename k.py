import pyautogui
import time
import os
import subprocess

{with open(".\\k.txt") as t:
    k=t.readlines()
    #os.system('start cmd')
    print(k)
    for i in k:
        pyautogui.typewrite(i,shell=True)    
        time.sleep(1)}

//add this 