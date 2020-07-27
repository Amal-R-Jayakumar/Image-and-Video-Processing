# THERE ARE CODE LINES IN COMMENT FOR EACH PURPOSES.
# READ CAREFULLY
import cv2
#OBJECTS
# 1. video
# 2. FourCC_Codec
# 3. save
# These objects help process the video capturing
cam_port=0  #change it to 1 for normal webcams
video=cv2.VideoCapture(cam_port) 
#codec_id='XVID'
#FourCC_Codec=cv2.VideoWriter_fourcc(*codec_id)        #Video codec definition from FourCC Website. the * denote multiple arg entry like *arg
#save=cv2.VideoWriter('Web Cam Video Output file.avi',FourCC_Codec,30.0,(640,480))# video file saved through "save object".
#arg 1 = video output file name
#arg 2 = the file CODEC
#arg 3 = frame rate
#arg 4 = frame size of the video in the form of a tuple
while video.isOpened(): #works if the "cam_port" variable has the right port
    ret,frame = video.read() #frame reads video. ret is boolean
    if ret==True:    
    #    save.write(frame) # saving the file
    #    grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #greyscale output conversion
        cv2.imshow('Video Palyer',frame)   #colour video
    #    cv2.imshow('frame',grey)   #grayscale video
        k = cv2.waitKey(1) & 0xFF
        if  k  == ord('q') or k%256 == 27: 
            # "& 0xFF" is given for 64 bit operating systems. Haven't figured out why......yet.
            break
        elif k % 256 == 32 or k == ord('s'):
            cv2.imwrite("Capture.png", frame)
            
            video.release()
            cv2.destroyAllWindows()
    else:
        break
video.release() 
#save.release()
cv2.destroyAllWindows()
