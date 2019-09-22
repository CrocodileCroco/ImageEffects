import numpy as np 
import sys
from PIL import Image
import os
import random
gfil = input("Filename of the image? (in the current directory) : ")
im = Image.open(gfil)
data = np.asarray(im)
print(data)
width, height = im.size
img = Image.new('RGB', (width, height), color = 'white')
pixels = img.load()
geff = input("Choose effect (blackout, replica, spark, glitched, air) : ")
if geff == "blackout":
    for i in range(width):
        for j in range(height):
            effr = random.randint(0,2)
            if effr == 2:
                pixels[i,j] = (0,0,0)
            else:
                pixels[i,j] = tuple(data[j,i])
if geff == "spark":
    for i in range(width):
        for j in range(height):
            effr = random.randint(0,1)
            if effr == 1:
                pixels[i,j] = (251,14,255)
            else:
                pixels[i,j] = tuple(data[j,i])
if geff == "glitched":
    alternateg = 0
    currentheight = 0
    for i in range(width):
        if alternateg == 0:
            for j in range(height):
                pixels[i,j] = tuple(data[j,i])
        if alternateg == 1:
            z = height - 1
            j = 0
            while z != 0:
                pixels[i,j] = tuple(data[z,i])
                z = z - 1
                j = j + 1
        alternateg = alternateg + 1
        if alternateg == 2:
            alternateg = 0
        currentheight = currentheight + 1
if geff == "air":
    toggleair = 0
    toggleuse = 0
    for i in range(width):
        toggleair = 0
        if toggleuse == 0:
            for j in range(height):
                if toggleair == 2:
                    pixels[i,j] = tuple(data[j,i])
                toggleair = toggleair + 1
                if toggleair == 3:
                    toggleair = 0
        toggleuse = toggleuse + 1
        if toggleuse == 2:
            toggleuse = 0
else:
    for i in range(width):
        for j in range(height):
            pixels[i,j] = tuple(data[j,i])
cwd = os.getcwd()
goutp = input("Output filename : ")
img.save(cwd + "/" + goutp)