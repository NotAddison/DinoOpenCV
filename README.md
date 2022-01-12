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

### Configure PIP (optional)
- [Configure Pyhon](https://datatofish.com/add-python-to-windows-path/)



### Virtual Environment (venv)
```
Install >> pip install virtualenv
create >> cd to folder, python -m venv (name)
Activation >> .\(name)\Scripts\activate
```

### Installing Libaries
* OpenCV (cv2, Computer Vision):
	>pip install opencv-python

* Numpy (Math ; array)
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
### Known problems : <br>
<details>
    <summary><b>FPS tanking when cactus is detected</b></summary>
    <p>I have no idea how to solve this lol</p>
</details>

<details>
    <summary><b>Dino Jump Timing (offset)</b></summary>
    <p>Possibly due to variation in the game speed & FPS drops causing delays in the template matching algo ; resulting in delayed input</p>
</details>
  
----------------------------------
### Documentations :
<b>Good YouTube Tutorial 👍:</b><br>
- [OpenCV Object Detection](https://www.youtube.com/watch?v=KecMlLUuiE4&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI&index=1) <br>
- [PyAutoGui Screen & Mouse Position](https://pyautogui.readthedocs.io/en/latest/mouse.html)


