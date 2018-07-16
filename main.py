from PIL import Image
import Palette



blankimg = Image.new("RGB",(100,100))

for i in range(100):
    for j in range(100):
        blankimg.putpixel((i,j),Palette.BRIGHT.genColor())

blankimg.save("blankimg.png")