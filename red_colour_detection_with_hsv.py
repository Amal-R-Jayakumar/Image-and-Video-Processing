import cv2
import numpy as np


capture=cv2.VideoCapture(0)

while capture.isOpened():
    ref,frame=capture.read()
    grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey_frame=cv2.cvtColor(grey_frame,cv2.COLOR_GRAY2BGR)


    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    red_lower_range=np.array([0,100,150])
    red_upper_range=np.array([40,255,255])
    red_mask=cv2.inRange(hsv_frame, red_lower_range, red_upper_range)
    red_colour=cv2.bitwise_and(hsv_frame,hsv_frame,mask=red_mask)
    red_mask_image=cv2.add(red_colour,grey_frame)
    
    
    if ref == True:
        cv2.imshow('frame',frame)
        cv2.imshow("red",red_mask_image)
        cv2.imshow("hsv",hsv_frame)
        k=cv2.waitKey(1) & 0xFF
        if k%256 == 27 or k == ord('q'):
            break
        
capture.release()
cv2.destroyAllWindows()
