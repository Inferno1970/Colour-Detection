import cv2
from PIL import Image
import numpy as np

from MyUtil import get_limits

yellow=[0,255,255]  #In BGR color space

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Couldn't open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read frame")
        break
    #It is used to convert an image from one color space to another
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 
    #In hsv color space we need to have a range of 
    #a specific color that we can get with util function
    lowerLimit, upperLimit=get_limits(color=yellow)
    mask=cv2.inRange(hsvImage,lowerLimit, upperLimit) 
    #Convering our array to pillow
    mask_=Image.fromarray(mask)
    #Getting bounding box locations
    bbx=mask_.getbbox()
    if bbx is not None:
        x1,y1,x2,y2=bbx
        #Showing our bounding box in frames
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    #cv2.imshow('frame',mask)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()