from PIL import Image
img=Image.open("ramz_aks_encode.png")
text=""
for i in range(0,img.size[0],5):
    for j in range(0,img.size[1],5):
        r,g,b=img.getpixel((i,j))
        if r==0:
            break
        text+=chr(r)
    if r==0:
        break
print(text)