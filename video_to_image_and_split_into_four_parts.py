'''video_to_image_and_split_into_four_parts program captures image from webcam and cuts it into four equal parts. 
The VideoCapture object is named video. 
The webcam port can be changed according to the need by changing the value of "web_cam_port" in line 54 to -1 or 1 for default webcam. 
it is usually 0 When the object "video" recieves input, the value of "video.isOpened()" becomes TRUE. 
Here "frame" is the video matrix in the while loop. 
When the webcam feed is opened, the user can choose to quit by pressing 'q' or the 'ESC' key. 
This will delete the video matrix and the program will be terminated. 
If the user wants to capture image, press 'SPACE' or 's' Key. 
This action will capture the image. The image is saved as 'Capture.png'. 
Then the function to crop images will take over and save and display 4 individual images. 
The images are created by taking 'Capture.png' into a matrix named'image'. 
'Height' and 'Width' of the capture is read and a new matrix named 'crop' is created each time changing the dimensions. 
The cropped images will be displayed. Then press 'q' or 'ESC' to close the windows.'''



import cv2
def crop_image_into_four(image_file):   
    image = cv2.imread(image_file)
    height, width = image.shape[:2]
    y=0
    x=0
    h=height//2
    w=width//2
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_1.jpg', crop) 
    cv2.imshow('Image_1.jpg',crop)
    y=height//2
    x=0
    h=height
    w=width//2
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_2.jpg', crop)
    cv2.imshow('Image_2.jpg',crop)
    y=0
    x=width//2
    h=height//2
    w=width
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_3.jpg', crop)
    cv2.imshow('Image_3.jpg',crop)
    y=height//2
    x=width//2
    h=height
    w=width
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_4.jpg', crop)    
    cv2.imshow('Image_4.jpg',crop)
    key = cv2.waitKey(0) & 0xFF
    if key % 256 == 27 or k == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        

web_cam_port=0  
video=cv2.VideoCapture(web_cam_port) 
while #only using OpenCV.                        
import cv2
def crop_image_into_four(image_file):                   # Function to crop image captured into four equal part
    image = cv2.imread(image_file)                      # Converting the image file into a matrix. use 'print(image)' to see the matrix
    height, width = image.shape[:2]                     # The variables height and width contains the number of rows and columns in the image.
    
    # The first portion is cut of from here. The method used is to call the matrix of the required part 
    # and write it as an image. 
    
    y=0
    x=0
    h=height//2
    w=width//2
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_1.jpg', crop) 
    cv2.imshow('Image_1.jpg',crop)
    
    # The second portion is cut of from here
    
    y=height//2
    x=0
    h=height
    w=width//2
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_2.jpg', crop)
    cv2.imshow('Image_2.jpg',crop)
    
    # The Third portion is cut of from here
    
    y=0
    x=width//2
    h=height//2
    w=width
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_3.jpg', crop)
    cv2.imshow('Image_3.jpg',crop)
    
    # The fourth Portion 
    
    y=height//2
    x=width//2
    h=height
    w=width
    crop = image[y:y+h, x:x+w]
    cv2.imwrite('Image_4.jpg', crop)    
    cv2.imshow('Image_4.jpg',crop)
    
    # press 'q' or 'esc' key to close the open images.
    key = cv2.waitKey(0) & 0xFF
    if key % 256 == 27 or k == ord('q'):
        video.release()
        cv2.destroyAllWindows()

web_cam_port=0                          # use the IDs 0 or -1 to connect to the default webcam. External webcams are usually taken as 1 
video=cv2.VideoCapture(web_cam_port)    #video object is created
while video.isOpened():             
    ret,frame = video.read()            #frame reads video object. ret is return(boolean value).
    if ret==True:
        cv2.imshow('Video Palyer',frame)
        k = cv2.waitKey(1) & 0xFF
        if  k  == ord('q') or k%256 == 27:          #Press q or press Escape key to cancel
            # "& 0xFF" is given for 64 bit operating systems. Haven't figured out why......yet.
            break
        elif k % 256 == 32 or k == ord('s'):        #Press Space bar key or 's' key to capture and save an image and cut it.
            cv2.imwrite("Capture.png", frame)       #image is captured and saved
            crop_image_into_four("Capture.png")     #function call to cut image into 4 parts.
            video.release()
            cv2.destroyAllWindows()                 
    else:
        break
video.release()
cv2.destroyAllWindows()
: 
    ret,frame = video.read() 
    if ret==True:
        cv2.imshow('Video Palyer',frame)
        k = cv2.waitKey(1) & 0xFF
        if  k  == ord('q') or k%256 == 27: 
            # "& 0xFF" is given for 64 bit operating systems. Haven't figured out why......yet.
            break
        elif k % 256 == 32 or k == ord('s'):
            cv2.imwrite("Capture.png", frame)
            image_file='Capture.png'
            crop_image_into_four(image_file)
            video.release()
            cv2.destroyAllWindows()
    else:
        break
video.release()
cv2.destroyAllWindows()
