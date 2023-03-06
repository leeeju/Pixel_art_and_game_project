from PIL import Image
import os

os.chdir("C://Users//user//Desktop")
work = Image.open('작업 블라썸.jpg')
work.show()
work = Image.new("RGB",(500,500),(125,255,125))
work1 = work.load()
width, height = work.size

for i in range(0,width):
    for j in range(0,height):
        color = (i+j)*255/(width+height)
        work1[i,j] = (125,int(color),125)
work.show()        