
import pyautogui
import time


while True:

    pos = pyautogui.locateCenterOnScreen('dark_drop_el.png')
    if pos:
        print pos
        pyautogui.moveTo(pos)
        pyautogui.click()

    pos = pyautogui.locateCenterOnScreen('drop_el.png')
    if pos:
        print pos
        for p in pos:
            pyautogui.moveTo(p)
            pyautogui.click()
            time.sleep(1)

    pos = pyautogui.locateCenterOnScreen('play.png')
    if pos:
        print pos
        pyautogui.moveTo(pos)
        pyautogui.click()

    time.sleep(1)