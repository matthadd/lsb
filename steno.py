import numpy as np
from PIL import Image


def encode(source, message, destination):
    source = 'images.jpg'
    message = 'test'
    destination = 'out.jpg'

    image = Image.open(source, 'r')
    width, height = image.size
    print('[+] lsb start')
    data = np.array(image)  # (list(image.getdata()))
    message += 'stenoEOF'

    message = 'testa'
    message_b = ''.join([format(ord(i), "08b") for i in message])
    print(message_b)

    def hide(data):
        index = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                for k in range(len(data[0, 0])):
                    var = format(data[i, j, k], "08b")
                    var = var[:-1] + str(message_b[index])
                    index += 1
                    var = int(var, 2)
                    data[i, j, k] = var
                    if index == len(message_b):
                        return None
    hide(data)

    def dehide(data):
        message_b = ''
        index = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                for k in range(len(data[0, 0])):
                    number =  data[i,j,k]
                    number = format(number, "08b")
                    message_b += number[-1]

        return message_b

    message_b = dehide(data)
    print(message_b)


    img = Image.fromarray(data, 'RGB')
    img.save(destination)
    img.show()

    print('[+] lsb end')


source = ""
message = ""
destination = ""
encode(source, message, destination)
