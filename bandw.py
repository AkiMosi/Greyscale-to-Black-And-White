from PIL import Image
im= Image.open('img1.jpg')
pixelMap=im.load()
img=Image.new(im.mode,im.size)
pixelsNew=im.load()
for i in range (img.size[0]):
    for j in range(img.size[1]):
        if(pixelMap[i,j]<(127)):
            pixelMap[i,j]=(0)
        elif(pixelMap[i,j]>=(127)):
            pixelMap[i,j]=(255)
im.show()