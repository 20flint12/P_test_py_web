import pyautogui

pos = pyautogui.locateCenterOnScreen('cross.png')
if pos:
    print pos
    pyautogui.moveTo(pos)
    pyautogui.click()

pos = pyautogui.locateCenterOnScreen('next.png')
if pos:
    print pos
    pyautogui.moveTo(pos)
    pyautogui.click()

pos = pyautogui.locateCenterOnScreen('play.png')
if pos:
    print pos
    pyautogui.moveTo(pos)
    pyautogui.click()
