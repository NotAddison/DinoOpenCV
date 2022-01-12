# DinoOpenCV
```
+==================================================================+
|   ___   _ __              ___ __   __       ___   _              |
|  / _ \ | '_ \ ___  _ _   / __|\ \ / /      |   \ (_) _ _   ___   |
| | (_) || .__// -_)| ' \ | (__  \   /       | |) || || ' \ / _ \  |
|  \___/ |_|   \___||_||_| \___|  \_/        |___/ |_||_||_|\___/  |
|                                                                  |
|   Link to game : chrome://dino/   	               By: Addison |
+==================================================================+
```  
-----------------------------------
## TOC   
 
-----------------------------------
### Configure PIP (optional)




### Virtual Environment (venv)
```
Install >> pip install virtualenv
create >> cd to folder, python -m venv (name)
Activation >> .\(name)\Scripts\activate
```

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
<details>
    <summary><b>Pyautogui vs PIL.ImageGrab</b></summary>
    <p>pyautogui captures the full screen, ImageGrab can capture a <u>specific part</u> of a screen.</p>
</details>

