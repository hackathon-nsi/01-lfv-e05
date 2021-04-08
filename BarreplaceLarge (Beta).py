#Beta "BarreplaceLarge"

from PIL import Image
from IPython.display import display
import urllib.request
#programme fait par Nicolas vdv
# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))
im_3=Image.open("Capture_hackathon.PNG")
# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (500, 500), (255, 255, 255))

# informations sur l'image
print(im_3.format, im_3.size, im_3.mode)

# taille de l'image
width, height = im.size

# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
def barreplace ():
    barreplacelarge= input ("largeur de la bande")
    for y in range(0,448):
        for x in range(0,356):
            pixel = im_3.getpixel((x, y))
            p_rouge = pixel[0]
            p_vert =  pixel[1]
            p_bleu =  pixel[2]
             #if change taille de bande
             #x change la distance bande-reste (si deplacement à l'arriere de premiere bande x=x-(distance attendue-1) )
             #y monte/decent la barre


            if 0<x<0+barreplacelarge:
                im_new.putpixel((x+barreplacelarge,y+10),(p_rouge,p_vert,p_bleu))
            elif barreplacelarge+x<x<(barreplacelarge*2)+x:
                im_new.putpixel((x-barreplacelarge,y+5),(p_rouge,p_vert,p_bleu))
            elif barreplacelarge+x<x<(barreplacelarge*2)+x:
                im_new.putpixel((x+barreplacelarge,y+10),(p_rouge,p_vert,p_bleu))
            elif barreplacelarge+x<x<(barreplacelarge*2)+x:
                im_new.putpixel((x,y+5),(p_rouge,p_vert,p_bleu))
            elif barreplacelarge+x<x<(barreplacelarge*2)+x:
                im_new.putpixel((x-barreplacelarge*2,y+10),(p_rouge,p_vert,p_bleu))
            else:
                im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))



    # valeurs des couleurs rouge, vert, bleu
    ##p_rouge = pixel[0]
    ##p_vert =  pixel[1]
    ##p_bleu =  pixel[2]

    # modification du pixel de coordonnées x, y
    #im.putpixel((x,y),(r,g,b))

    # affichage de l'image

    #im.show()

barreplace()
im_new.show()    ##im_3.show()