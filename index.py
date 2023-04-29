from PIL import Image
import os
import time

frameFiles = os.listdir('./frames')

for i in range(len(frameFiles)):
    im = Image.open('./frames/frame-' + str(i) + '.png', "r")
    imageWidth = im.size[0]
    imageHeight = im.size[1]

    pixels = list(im.getdata().convert('RGB'))

    white = (255, 255, 255)
    black = (0, 0, 0)

    frame = ''

    for i in range(len(pixels)):
        if (pixels[i][0] * 0.21 + pixels[i][1] * 0.71 + pixels[i][2] * 0.8) < 127.5:
            frame += '  '
        else:
            frame += '..'

        if (i % imageWidth == 0):
            frame += '\n'

    os.system('clear')

    print(frame)

    time.sleep(0.02)
