import pandas as pd
import json
import process
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

with open('logging.txt') as f:
    store=f.read()
    
a=eval(store)

width=len(a[0])
height=len(a)

new_image = Image.new('RGB', (width, height))
data = new_image.load()

for y in range(height):
    for x in range(width):
        data[(x, y)] = (tuple(a[y][x]))

new_image.save('foo.png', 'png')
img=mpimg.imread('foo.png')
imgplot = plt.imshow(img)
plt.show()

res=process.main(a)