# DinoOpenCV   
Link to game : chrome://dino/			   
By: Chua Jie Yi, Addison

### Configure PIP (optional)




### Virtual Environment (venv)
	Install >> pip install virtualenv
	create >> cd to folder, python -m venv (name)
	Activation >> .\(name)\Scripts\activate


### Installing Libaries
* OpenCV (cv2, Computer Vision):
	>pip install opencv-python

* Numpy (Math)
    >pip install numpy

* Pillow (Screencap)
    >pip install --upgrade Pillow

* PyAutoGui (Inputs)
    >pip install pyautogui


### Importing Libaries
```
#OpenCV (CV)
import cv2 
import numpy as np
import time

#Pillow (Screencap)
from PIL import Image, ImageGrab

#Pyautogui (Input)
import pyautogui as pag
```



-----------------------------------
Misc : <br>
Pyautogui vs PIL.ImageGrab : <br>
>pyautogui captures full screen, ImageGrab can grab a specific part of a screen.

