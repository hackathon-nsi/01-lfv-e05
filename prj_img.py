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

# la fonction "triangle" permet de couper des triangles dans les 4 cotes

def triangles():

img_arr[0 : 50, 0 : 50] = (255, 255, 255)
img_arr[315 : 50, 315 : 50] = (255, 255, 255)
img_arr[315 : 392, 315 : 392] = (255, 255, 255)
img_arr[50 : 392, 50 : 392] = (255, 255, 255)
img = Image.fromarray(img_arr)

#La fonction "sombre" permet de changer les couleur pls sombre

def sombre():

   im_data = im.load()
height,width = im.size
for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = im_data[loop1,loop2]
        im_data[loop1,loop2] = r//2,g//2,b//2
im_new.save('changed.jpeg')

triangles()
sombre()
img.show()
