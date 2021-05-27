import cv2
import numpy as np
def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('RGB-VALUES')

# create trackbars for color change
cv2.createTrackbar('R','RGB-VALUES',0,255,nothing)
cv2.createTrackbar('G','RGB-VALUES',0,255,nothing)
cv2.createTrackbar('B','RGB-VALUES',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 :OFF\n1: ON'
cv2.createTrackbar(switch, 'RGB-VALUES',0,1,nothing)
while(1):
    cv2.imshow('RGB-VALUES',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
# get current positions of four trackbars
    r = cv2.getTrackbarPos('R','RGB-VALUES')
    g = cv2.getTrackbarPos('G','RGB-VALUES')
    b = cv2.getTrackbarPos('B','RGB-VALUES')
    s = cv2.getTrackbarPos(switch,'RGB-VALUES')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()