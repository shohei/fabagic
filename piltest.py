from PIL import Image, ImageDraw
import time
im = Image.new('RGBA', (1000, 800), (255,255,255, 0)) 
draw = ImageDraw.Draw(im) 
#draw.line((100,200, 150,300), fill=128)
#im.show()
im.show()

for i in range(10):
    draw.line((100+10*i,200+10*i, 150+10*i,300+10*i), fill=128)
    im.update()
    time.sleep(1)

