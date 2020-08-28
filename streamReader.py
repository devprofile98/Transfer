import cv2 as cv
import numpy as np


vid = cv.VideoCapture("vid.mp4")

while True:
    ret, frame = vid.read()

    # gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow("frame", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
vid.release()
cv.destroyAllWindows()