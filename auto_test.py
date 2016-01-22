__author__ = 'sergey'


# import pyautogui
# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
# print currentMouseX, currentMouseY
# pyautogui.moveTo(100, 150)
# pyautogui.click()
#
#
# im1 = pyautogui.screenshot()
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



from Tkinter import *

root = Tk()

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()