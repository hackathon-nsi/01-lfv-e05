#-------------------------------------------------------------------------------
# Name:        prj img
# Purpose:
#
# Author:      Yassine
#
# Copyright:   (c) Yassine 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PIL import Image
from IPython.display import display
import urllib.request

#programme de Yassine

from PIL import Image
import numpy as np
img = Image.open("pictures/Capture_hackathon.PNG").convert('RGB')
img_arr = np.array(img)

#Cette fonction permet de couper des triangles dans les 4 cotes

img_arr[0 : 50, 0 : 50] = (255, 255, 255)
img_arr[315 : 50, 315 : 50] = (255, 255, 255)
img_arr[315 : 392, 315 : 392] = (255, 255, 255)
img_arr[50 : 392, 50 : 392] = (255, 255, 255)
img = Image.fromarray(img_arr)

#sdgösldmgspkdngsdg

for x in range(img.size[0]):
    for y in range (pic.size[1]):
        r, g , b =omg.getpixel((x,y))
        img.putpixel((x,y),(r//2 , g//2 , b//2))

img.show()
