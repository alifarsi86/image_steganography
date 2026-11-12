from PIL import Image
img=Image.open("ramz_aks.jpg")
text=input("enter the text: ")
index=0
done=False
for i in range(0,img.size[0],5):
    for j in range(0,img.size[1],5):
        if index<len(text):
            r,g,b=img.getpixel((i,j))
            char=text[index]
            ascii_code=ord(char)
            img.putpixel((i,j),(ascii_code,g,b))
            index+=1
        else:
            r,g,b=img.getpixel((i,j))
            img.putpixel((i,j),(0,g,b))
            done=True
            break
    if done:
        break

img.save("ramz_aks_encode.png")
