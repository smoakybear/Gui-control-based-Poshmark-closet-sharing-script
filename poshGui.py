#!python3
# Made to share poshmark listings in order. Doesn't work very well.

import pyautogui as gui
gui.PAUSE = 1
gui.FAILSAFE = True #drag mouse to the top left of the screen to stop the script

gui.scroll(-752)

while True:
    gui.leftClick(744, 1026)
    gui.leftClick(959, 396)
    gui.leftClick(1012, 1026)
    gui.leftClick(959, 396)
    gui.leftClick(1284, 1026)
    gui.leftClick(959, 396)
    gui.leftClick(1557, 1026)
    gui.leftClick(959, 396)
    gui.scroll(-752)