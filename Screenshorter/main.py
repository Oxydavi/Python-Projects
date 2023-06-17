import time
import pyautogui as pg
import keyboard as kb

folder_path = 'C:\\Screenshots'


def zxc(qwe):
    if qwe.name == 'print screen':
        screenshot = pg.screenshot()
        screenshot.save(f'{folder_path}\\{round(time.time(), 0)}.png')
        print(f"Скриншот {time.time(), 0} сохранен.")


kb.on_press(zxc)
kb.wait()


