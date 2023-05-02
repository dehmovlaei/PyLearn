import os
import imageio

fileList = sorted(os.listdir('08/image2Gif'))
IMAGES =[]
for fileName in fileList:
    filePath = '08/image2Gif/' + fileName
    image = imageio.imread(filePath)
    IMAGES.append(image)
imageio.mimsave('08/myGif.gif', IMAGES, loop=0)