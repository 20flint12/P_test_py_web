# coding: utf8
#!/usr/bin/python

import pprint

import pyautogui


__author__ = 'sergey'


import sys
# # export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
# # export PYTHONPATH=/usr/lib/python2.7/site-packages:$PYTHONPATH
#
# # /usr/lib/python2.7/dist-packages/cv2.so
# sys.path.append('/usr/lib/python2.7/site-packages')

pprint.pprint(sys.path)

# ***********************************


import pyscreeze


import time


import cv2
import numpy as np
from matplotlib import pyplot as plt





# im0 = pyautogui.screenshot()
# x = im0.convert()
# img2 = x.copy()
# plt.subplot(121),plt.imshow(img2)
#
# template = cv2.imread('template.png')
# plt.subplot(122),plt.imshow(template)
#
# plt.show()
#
# # Apply template Matching
# res = cv2.matchTemplate(img2,
#                         template,
#                         cv2.TM_CCOEFF)
# print res




# im1 = pyautogui.screenshot()
# print "1_im1=", im1
# print "2_im1=", im1.getdata()
# print "2_im1=", im1.size
#
# # cv2.imshow('win', im1.getdata)
# printscreen_numpy = np.array( im1.getdata(),dtype=np.uint8).reshape(
#         (im1.size[1],
#          im1.size[0],3))
# cv2.imshow('window',printscreen_numpy)
#
# im1.save('my_screenshot.png')
# # im2 = pyautogui.screenshot('my_screenshot2.png')
#
# time.sleep(20)




def getPosition(file_template):

    img = cv2.imread('my_screenshot.png',0)
    img2 = img.copy()

    template = cv2.imread(file_template,0)
    w, h = template.shape[::-1]


    # All the 6 methods for comparison in a list
    methods = [
               # 'cv2.TM_CCOEFF',
               'cv2.TM_CCOEFF_NORMED',
               # 'cv2.TM_CCORR',
               # 'cv2.TM_CCORR_NORMED',
               # 'cv2.TM_SQDIFF',
               # 'cv2.TM_SQDIFF_NORMED'
               ]

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        # print res
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # print min_val, max_val, min_loc, max_loc

        # if max_val > 0.95:
        return max_val, max_loc

        # # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        #     top_left = min_loc
        # else:
        #     top_left = max_loc
        # bottom_right = (top_left[0] + w, top_left[1] + h)
        #
        # cv2.rectangle(img,top_left, bottom_right, 255, 2)
        #
        # plt.subplot(121),plt.imshow(res,cmap = 'gray')
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(img,cmap = 'gray')
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.suptitle(meth)
        #
        # plt.show()





if __name__ == '__main__':

    pos = 0

    while True:

        im1 = pyautogui.screenshot()
        im1.save('my_screenshot.png')
        pos += 1

        # pos = pyautogui.locateCenterOnScreen('dark_drop_el.png')
        max_val, max_loc = getPosition('drop_dark_el.png')
        print max_val, max_loc
        pyautogui.moveTo(max_loc)
        if max_val > 0.91:
            pyautogui.click()
            print "* dark"
            time.sleep(1)

        # pos = pyautogui.locateCenterOnScreen('drop_el.png')
        max_val, max_loc = getPosition('drop_el.png')
        print max_val, max_loc
        pyautogui.moveTo(max_loc)
        if max_val > 0.91:
            pyautogui.click()
            print "* pink"
            time.sleep(1)

        max_val, max_loc = getPosition('drop_gold.png')
        print max_val, max_loc
        pyautogui.moveTo(max_loc)
        if max_val > 0.91:
            pyautogui.click()
            print "* gold"
            time.sleep(1)

        max_val, max_loc = getPosition('reload.png')
        print max_val, max_loc
        pyautogui.moveTo(max_loc)
        if max_val > 0.91:
            pyautogui.click()
            print "*"
            time.sleep(5)
            pyautogui.moveTo(1000, 650)
            pyautogui.dragRel(-80, 300, duration=1)
            time.sleep(1)


        # rst = pos % 4
        # print rst
        # if rst == 0:
        #     pyautogui.moveTo(1000, 650)
        #     pyautogui.dragRel(-200, 0, duration=1)
        # elif rst == 1:
        #     pyautogui.moveTo(1000, 650)
        #     pyautogui.dragRel(0, 200, duration=1)
        # elif rst == 2:
        #     pyautogui.moveTo(1000, 650)
        #     pyautogui.dragRel(200, 0, duration=1)
        # elif rst == 3:
        #     pyautogui.moveTo(1000, 650)
        #     pyautogui.dragRel(0, -200, duration=1)



        # pyautogui.moveTo(1000, 650)
        # pyautogui.dragTo(1200, 690, duration=2)  # drag mouse to XY
        # pyautogui.dragRel(-200, -40, duration=2)  # drag mouse relative to its current position




        time.sleep(3)

    # print getPosition()