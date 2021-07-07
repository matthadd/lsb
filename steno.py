import numpy as np
from PIL import Image
from termcolor import colored


def decode_image():
    file_data = []
    for i in range(len(pixels)):
        # file_data.append(pixels[i])
        # print(file_data)
        for j in range(len(pixels[0])):
            for k in range(len(pixels[0][0])):
                # print(pixels[i][j][k])
                file_data.append(format(pixels[i][j][k], "b"))
                # print("--- %s seconds ---" % (time.time() - start_time))
                # print(file_data)
    print("file_data complete")


def inverse_decode_image():
    pass


def encode(source, message ):
    source = 'IMG_7834.jpeg'
    message = 'test'

    image = Image.open(source, 'r')
    width, height = image.size
    print('[+] lsb start')
    pixels = np.array(list(image.getdata()))
    print(pixels)
    message += 'stenoEOF'


source = ""
message = ""
encode(source, message)

