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
# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (500, 500), (255, 255, 255))


# taille de l'image
width, height = im.size

# Cette fonction permet de changer la couleur des pixels en haut et en bas de l´image

def bandes ():

    for y in range(250,300):
        for x in range(0,600):
            im_new.putpixel ((x, y) , (210,210,210))

    for y in range(600,750):
        for x in range(0,600):
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

# Cette fonction permet de mettre un filtre de couleur grise sur l´image

def gris (im):

    return im.convert("L")
if __name__ == "__main__":
    with image.open('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp') as im:
        im = im.convert("RGBA")
        greyscale_im = greyscale(im)
        greyscale_im.save('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp')

    # affichage de l'image

    #im.show()

bandes()
coller()
gris(ss)
im_new.show()