__author__ = 'sergey'


import pyautogui

pyautogui.PAUSE = 0.5

screenWidth, screenHeight = pyautogui.size()
print "screenWidth, screenHeight=", screenWidth, screenHeight

currentMouseX, currentMouseY = pyautogui.position()
print currentMouseX, currentMouseY

pyautogui.moveTo(1250, 593)
pyautogui.click()


pyautogui.moveTo(1000, 650)
pyautogui.click()

pos = pyautogui.locateCenterOnScreen('looksLikeThis.png')
print
pyautogui.moveTo(pos)
pyautogui.click()

pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds

pyautogui.click()
pyautogui.typewrite('Hello world!\n', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character

im1 = pyautogui.screenshot()
# im1.save('my_screenshot.png')
# im2 = pyautogui.screenshot('my_screenshot2.png')



# sudo apt-get install python-pygame


#
# import pygame
#
# pygame.init()
# pygame.display.set_mode()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit(); #sys.exit() if sys is imported
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_0:
#                 print("Hey, you pressed the key, '0'!")
#             if event.key == pygame.K_1:
#                 print("Doing whatever")
#



# while True:
#
#     keys=pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         if count == 10:
#             location-=1
#             count=0
#         else:
#             count +=1
#         if location==-1:
#             location=0
#
#     if keys[pygame.K_RIGHT]:
#         print "34534534"
#         if count == 10:
#             location+=1
#             count=0
#         else:
#             count +=1
#         if location==5:
#             location=4



# from Tkinter import *
#
# root = Tk()
#
# def key(event):
#     print "pressed", repr(event.char)
#
# def callback(event):
#     frame.focus_set()
#     print "clicked at", event.x, event.y
#
# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()
#
# root.mainloop()



