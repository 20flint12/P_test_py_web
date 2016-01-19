__author__ = 'sergey'


import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print currentMouseX, currentMouseY
pyautogui.moveTo(100, 150)
pyautogui.click()


im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')
im2 = pyautogui.screenshot('my_screenshot2.png')


