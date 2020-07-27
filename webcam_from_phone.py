import urllib.request
import cv2
import numpy as np
url_id='http://25.13.177.28:8080/shot.jpg'
while True:
    img_phone=urllib.request.urlopen(url_id)
    image_array=np.array(bytearray(img_phone.read()),dtype=np.uint8)
    image=cv2.imdecode(image_array,-1)
    grey_frame=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    grey_frame=cv2.cvtColor(grey_frame,cv2.COLOR_GRAY2BGR)
    hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)                         ## The HSV frame of the normal decoded image
    red_lower_1 = np.array([0,130,140])                                     ## The Colour Range(min) in the order Hue Saturation Brightness 
    red_upper_1 = np.array([40,255,255])                                    ## The Colour Range(max)
    red_mask_0=cv2.inRange(hsv_image, red_lower_1, red_upper_1)             ## Range of Colours to be identified
    red_colour_1 = cv2.bitwise_and(image,image,mask=red_mask_0)             ## Embedding
    grey=cv2.add(red_colour_1,grey_frame)
    cv2.imshow('grey',grey)
    cv2.imshow('image viewer',image)
    i=1
    if red_mask_0.any() == True:                                        
        cv2.imwrite(f'files/grey{i}.jpg',grey)
        i+=1
    k= cv2.waitKey(1)   
    if k % 256 == 27 or k ==ord('q'):
        cv2.destroyAllWindows() 
        break
    elif k % 256 == 32 or k == ord('s'):
        cv2.imwrite('new capture.png',image)
cv2.destroyAllWindows()
