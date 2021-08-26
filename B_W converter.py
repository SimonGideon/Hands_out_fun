wqeq3import pip
import PIL

from PIL import Image

img= Image.open("D:\PICTURES\hahaha.png")
blackAndWhite = img.convert("L")
blackAndWhite.save('D:\PICTURES\Bw_hahaha.png')
blackAndWhite.show()
