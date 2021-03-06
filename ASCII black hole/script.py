from PIL import Image, ImageDraw, ImageFont

import math

characters = "blackhole"[::-1]

charArray = list(characters)
charLength = len(characters)
interval = charLength/256

scaleFactor = 0.2
oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("result.txt", "w")

im = Image.open("blackhole.jpg")

ft = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

result_Image = Image.new('RGB', (oneCharWidth*width, oneCharHeight*height), color = (0, 0, 0))
d = ImageDraw.Draw(result_Image)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i]= (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = ft, fill = (r, g, b))
    text_file.write('\n')

result_Image.save("result.png")