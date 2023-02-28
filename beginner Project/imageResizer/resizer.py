from PIL import Image


def resize_image(size1, size2):
    img = Image.open("oldImage.jpeg")
    #print(img.size)

    resize_img = img.resize((size1, size2))
    resize_img.save('new_image.jpg')


size1 = int(input('Enter Length size: '))
size2 = int(input('Enter Width Size: '))
resize_image(size1, size2)