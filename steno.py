import numpy as np
from PIL import Image


def encode(source, message, destination):
    source = 'images.jpg'
    message = 'test'
    destination = 'out.jpeg'

    image = Image.open(source, 'r')
    width, height = image.size
    print('[+] lsb start')
    data = np.array(list(image.getdata()))
    message += 'stenoEOF'

    print('')
    print(data)
    print(width * height, width, height)


    img = Image.fromarray(data, 'RGB')
    img.save(destination)
    img.show()

    print('[+] lsb end')


source = ""
message = ""
destination = ""
encode(source, message, destination)
