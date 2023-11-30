import pyautogui
import math
import time

time.sleep(2)
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.dragRel(250, 0, duration = 0.5)
pyautogui.mouseDown()
for i in range(0,60):
    x = currentMouseX+math.cos(i*6*(math.pi/180))*250
    y = currentMouseY+math.sin(i*6*(math.pi/180))*250
    pyautogui.moveTo(x, y, duration = 0.01)

pyautogui.mouseUp();
    
    
