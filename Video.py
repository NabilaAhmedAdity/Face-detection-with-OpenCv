import numpy as np
import cv2

cap = cv2.VideoCapture(0)

scale_factor = 1.1
min_neighbors = 3
min_size = (30, 30)
flags = cv2.cv.CV_HAAR_SCALE_IMAGE

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cnt = 60
while(cnt):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Apply haar-like feature and crop the face
    faces = face_cascade.detectMultiScale(gray, scaleFactor = scale_factor, minNeighbors = min_neighbors, minSize = min_size, flags = flags)
    print "How many faces: " + str(len(faces))
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        #cv2.imshow("cropped", crop_img)
        file_name = "./crop" + (str)(60-cnt) + ".jpg"
        cv2.imwrite( file_name, crop_img);
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cnt = cnt-1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
