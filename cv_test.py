# coding: utf8
#!/usr/bin/python

__author__ = 'sergey'

import os
import numpy as np
import cv2
import time
import pprint

from datetime import datetime

string_date = "rec_2016-11-24_00-22.mkv"
res = datetime.strptime(string_date, "rec_%Y-%m-%d_%H-%M.mkv")
print(res)


# ***********************************

# import sys
#
# # sys.path.append('/usr/local/lib/python2.7/site-packages')
# sys.path.append('/usr/lib/python2.7/dist-packages')

# import sys

# sys.path.append('/usr/local/lib/python2.7/site-packages')
# sys.path.append('/usr/lib/python2.7/dist-packages')



# # Create a black image
# img = np.zeros((512,512,3), np.uint8)
#
# # Draw a diagonal blue line with thickness of 5 px
# cv2.line(img,(0,0),(511,511),(255,0,0),5)
#
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#
# cv2.circle(img,(447,63), 63, (0,0,255), -1)
#
#
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ********************************
#
# import cv2
# import numpy as np
#
# def nothing(x):
#     pass
#
# # Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
# cv2.namedWindow('image')
#
# # create trackbars for color change
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)
#
# # create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image',0,1,nothing)
#
# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
#     # get current positions of four trackbars
#     r = cv2.getTrackbarPos('R','image')
#     g = cv2.getTrackbarPos('G','image')
#     b = cv2.getTrackbarPos('B','image')
#     s = cv2.getTrackbarPos(switch,'image')
#
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b,g,r]
#
# cv2.destroyAllWindows()
#


# ***********************************


# cap = cv2.VideoCapture(0)
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


# ***********************************

path = '/home/flint/Videos/_cam_records/'
name_list = os.listdir(path)
# print(name_list)

full_list = [os.path.join(path, i) for i in name_list]
# pprint.pprint(full_list)

# time_sorted_list = sorted(full_list, key=os.path.getmtime)
time_sorted_list = sorted(full_list)
# pprint.pprint(time_sorted_list)

output_name = "compiled_" + time_sorted_list[0][36:-3] + "avi"
print "output_name=", output_name
fl = [
    'rec_2016-11-23_19-22.mkv',
    'rec_2016-11-23_20-22.mkv',
    'rec_2016-11-23_21-22.mkv',

    # 'rec_2016-11-23_22-22.mkv',
    # 'rec_2016-11-23_23-22.mkv',
    # 'rec_2016-11-24_00-22.mkv',
    # 'rec_2016-11-24_01-22.mkv',
    # 'rec_2016-11-24_02-22.mkv',
    # 'rec_2016-11-24_03-22.mkv',
    # 'rec_2016-11-24_04-22.mkv'
    # 'rec_2016-11-24_05-22.mkv',
    # 'rec_2016-11-24_06-22.mkv',
    # 'rec_2016-11-24_07-23.mkv',
    # 'rec_2016-11-24_08-23.mkv',

    # 'bike.avi',
    # 'rec_2016-11-25_07-23.mkv',
]


def diff_img(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter(output_name, fourcc, 15.0, (480, 640))

for f in time_sorted_list[:5]:
    print(f)
    cnt = 0

    try:
        cap = cv2.VideoCapture(f)
        time.sleep(0.2)
        img = cap.read()[0]
        time.sleep(0.2)

        t_minus = img
        t = img
        t_plus = img

        fgbg = cv2.BackgroundSubtractorMOG()

        while cap.isOpened():
            cnt += 1
            ret, frame = cap.read()
            diff_result = diff_img(t_minus, t, t_plus)
            count_black = cv2.countNonZero(diff_result)
            if count_black > 42000:
                print count_black, cnt
                out.write(frame)

            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # gray = cv2.GaussianBlur(gray, (21, 21), 0)

            fgmask = fgbg.apply(frame)
            cv2.imshow('BG frame', fgmask)

            # print diff_result
            cv2.imshow("Movement Indicator", diff_result)

            # Read next image
            t_minus = t
            t = t_plus
            t_plus = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            # t_plus = gray

            cv2.imshow('Origin frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except:
        print "errror"
        pass

cap.release()
cv2.destroyAllWindows()

out.release()


# # cam = cv2.VideoCapture(0)
# #
# # cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
# #
# # # Read three images first:
# # t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
# # t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
# # t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
# #
# # while True:
# #     cv2.imshow(winName, diff_img(t_minus, t, t_plus))
# #
# #     # Read next image
# #     t_minus = t
# #     t = t_plus
# #     t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
# #
# #     key = cv2.waitKey(10)
# #     if key == 27:
# #         cv2.destroyWindow(winName)
# #         break
# #
print "Goodbye"




# print PYTHONPATH

# ***********************************

# Saving a Video

# cap = cv2.VideoCapture(0)
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# fourcc = cv2.cv.CV_FOURCC(*'XVID')
# # out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
# out = cv2.VideoWriter('output.avi',fourcc, 5.0, (640,480))
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret==True:
#
#         frame = cv2.flip(frame,0)
#
#         if cv2.waitKey(1) & 0xFF == ord('n'):
#             # write the flipped frame
#             out.write(frame)
#
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()






# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_ml/py_knn/py_knn_opencv/py_knn_opencv.html

# from matplotlib import pyplot as plt
#
# img = cv2.imread('digit.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('frame', gray)
# cv2.waitKey(0)
#
#
#
# # Now we split the image to 5000 cells, each 20x20 size
# cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
#
# # Make it into a Numpy array. It size will be (50,100,20,20)
# x = np.array(cells)
#
# # Now we prepare train_data and test_data.
# train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
# test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
#
# # Create labels for train and test data
# k = np.arange(10)
# train_labels = np.repeat(k,250)[:,np.newaxis]
# test_labels = train_labels.copy()
#
# # Initiate kNN, train the data, then test it with test data for k=1
# knn = cv2.KNearest()
# knn.train(train,train_labels)
# ret,result,neighbours,dist = knn.find_nearest(test,k=5)
#
# # Now we check the accuracy of classification
# # For that, compare the result with test_labels and check which are wrong
# matches = result==test_labels
# correct = np.count_nonzero(matches)
# accuracy = correct*100.0/result.size
# print accuracy
#
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()












