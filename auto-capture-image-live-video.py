

import cv2
import time
  
 
# SET THE COUNTDOWN TIMER
TIMER = int(15)
  
# Open the camera
cap = cv2.VideoCapture(0)
  
 
while True:
     
    # Read and display each frame
    ret, img = cap.read()
    cv2.imshow('a', img)
 
    prev = time.time()
 
    while TIMER >= 0:
        ret, img = cap.read()
 
        # Display countdown on each frame
        # specify the font and draw the
        # countdown using puttext
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(TIMER),
                    (200, 250), font,
                    5, (0, 255, 255),
                    4, cv2.LINE_AA)
        cv2.imshow('a', img)
        cv2.waitKey(125)
 
        # current time
        cur = time.time()
 
        # Update and keep track of Countdown
        # if time elapsed is one second
        # than decrease the counter
        if cur-prev >= 1:
            prev = cur
            TIMER = TIMER-1
 
        else:
            ret, img = cap.read()
 
            cv2.imshow('a', img)
 
 
            # Save the frame
            cv2.imwrite('photo.jpg', img)

    break
 
# close the camera
cap.release()
  
# close all the opened windows
cv2.destroyAllWindows()
