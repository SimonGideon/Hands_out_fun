import PIL
import winsound
from PIL import Image

img = Image.open("D:\PICTURES\PO74763662.jpg")

blackAndWhite = img.convert("L")
blackAndWhite.save('D:\PICTURES\Bw_hahaha.png')
blackAndWhite.show()

if blackAndWhite:
    freq = 2500
    dur = 1000
    winsound.Beep(freq, dur)
else:
    print("gfgg")
