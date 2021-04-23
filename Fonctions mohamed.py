#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mouhamed
#
# Created:     26/03/2021
# Copyright:   (c) Mouhamed 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from PIL import Image
from IPython.display import display
import urllib.request
#programme de Mohamed
# ouvrir une image
im = Image.open("Capture_hackathon.PNG")
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (500, 500), (255, 255, 255))


# taille de l'image
width, height = im.size

# Cette fonction permet de changer la couleur des pixels en haut et en bas de l´image

def bandes ():

    for y in range(width):
        for x in range(15, 40):
            im_new.putpixel ((x, y) , (210,210,210))

    for y in range(width):
        for x in range(400, 423):
            im_new.putpixel ((x, y) , (255,255,255))

# Cette fonction permet de couper une partie de l´image et de la copier sur plusieurs partie de l´image

def coller ():

    croppedi= im.crop((168,80,431,420))
    croppedi.save('cropped.bmp')
    croppedi.size

    icopyIm= im.copy()
    icopyIm.paste(croppedi, (0,0))
    icopyIm.paste(croppedi, (250,300))
    icopyIm.paste(croppedi, (550,500))
    icopyIm.save('pasted.bmp')

# Cette fonction permet d´enlever la couleur rouge de l´image

def couleur (im):

    im_data = im.load()
height,width = im.size
for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = im_data[loop1,loop2]
        im_data[loop1,loop2] = 0,g,b
im_new.save('changed.jpeg')

    # affichage de l'image

    #im.show()

bandes()
coller()
gris()
im_new.show()
