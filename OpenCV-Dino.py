#OpenCV
import cv2 
import numpy as np
import time

#Screencap
from PIL import Image, ImageGrab

#Keyboard Emulation
import pyautogui as pag

while True:
    # ScreenGrabbing
    img = ImageGrab.grab(bbox=(400,400,800,800)) #bbox default = whole screen | (left_x, top_y, right_x, bottom_y)

    img_arry = np.array(img) # Convert Image to an array
    img_grey = cv2.cvtColor(img_arry, cv2.COLOR_BGR2GRAY) # Convert to greyscale
    cv2.imshow("",img_grey) # Show screencaptured images (videos = buch of photos (frames))

    # Compare Images
    template = cv2.imread(r'.\template\catc1.png',0) #0 parameter = read image in greyscale mode

    # Keyboard Input


    if cv2.waitKey(1) == 27: break #Keybaord key ID ; 27 = esc

cv2.destroyAllWindows()
