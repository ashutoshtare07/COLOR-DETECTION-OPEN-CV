import cv2 

from color import get_limits   

from PIL import Image

red = [0, 0, 255]  # BGR values for red
green = [0, 255, 0]  # BGR values for green
blue = [255, 0, 0]  # BGR values for blue

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(green)  # Choose the color you want to detect
    lowerLimit1, upperLimit1 = get_limits(blue) 
    lowerLimit2, upperLimit2 = get_limits(red) 

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask1 = cv2.inRange(hsvImage, lowerLimit1, upperLimit1)
    mask2 = cv2.inRange(hsvImage, lowerLimit2, upperLimit2)

    mask_ = Image.fromarray(mask)
    mask_1 = Image.fromarray(mask1)
    mask_2 = Image.fromarray(mask2)

    bbox = mask_.getbbox()
    bbox1 = mask_1.getbbox()
    bbox2 = mask_2.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    if bbox1 is not None:
           x1, y1, x2, y2 = bbox1

           frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    if bbox2 is not None:
        x1, y1, x2, y2 = bbox2

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
cv2.destroyAllWindows()