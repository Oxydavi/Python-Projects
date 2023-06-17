import time
import pyautogui as pg
import keyboard as kb
import sys
import mouse as ms
import threading

IsClicking = False
is_running = True


def do_click():
    while IsClicking:
        pg.click()
        time.sleep(0.01)


def change():
    global IsClicking
    IsClicking = not IsClicking
    if IsClicking:
        print("Start")
        threading.Thread(target=do_click).start()
    else:
        print("Stop")


def predochranitel():
    global is_running
    is_running = False
    sys.exit(0)


kb.add_hotkey("k", change)
kb.add_hotkey("l", predochranitel)

while is_running:
    pass
