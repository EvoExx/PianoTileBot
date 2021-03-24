from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#https://www.agame.com/game/magic-piano-tiles - this is the game
#pixels are based on a 1080p screen resolution and a left half screen window for the game
#tile1 X:  350 Y:  515 RGB: (174, 178, 234)
#tile2 X:  450 Y:  515 RGB: (133, 136, 169)
#tile3 X:  550 Y:  515 RGB: (  0,   0,   0)
#tile4 X:  650 Y:  515 RGB: (253,  18,   1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(350,515)[0] == 0:
        click(350,515)
    if pyautogui.pixel(450,515)[0] == 0:
        click(450,515)
    if pyautogui.pixel(550,515)[0] == 0:
        click(550,515)
    if pyautogui.pixel(650,515)[0] == 0:
        click(650,515)
