import numpy as np
from PIL import Image
from sys import argv

HEADER_SIZE = 32


class Hide():

    def __init__(self, file_name, image_source, image_output):
        self.file_name = file_name
        self.image_source = image_source
        self.image_output = image_output
        self.message_b = open(self.file_name, 'rb').read()

    def encode(self):
        print(self.message_b)
        image = Image.open(self.image_source)
        print('[+] lsb start write image')
        data = np.array(image)
        self.message_b = ''.join([format(i, "08b") for i in self.message_b])
        # header = format(len(self.message_b), "08b")
        header = '{:032b}'.format(len(self.message_b))
        print('input', header, ".", self.message_b)
        self.message_b = header + self.message_b

        def hide(data):
            index = 0
            for i in range(len(data)):
                for j in range(len(data[0])):
                    for k in range(len(data[0, 0])):
                        # print(data[i,j,k], end = " ")
                        var = format(data[i, j, k], "08b")
                        print(int(var, 2), var, end=" ")
                        var = var[:-1] + str(self.message_b[index])
                        print(self.message_b[index], var, int(var, 2), end=" ")
                        index += 1
                        var = int(var, 2)
                        data[i, j, k] = var
                        print(data[i, j, k])
                        if index == len(self.message_b):
                            return None

        print(data)
        hide(data)
        data[0, 0, 0] = 0
        print(data)
        im = Image.fromarray(data)
        im.save(image_output)
        # im.show()
        print('[+] Finish writing data to image')


class Dehide():
    def __init__(self, image_output):
        self.image_output = image_output
        self.message_b = ''

    def dehide(self):
        image = Image.open(self.image_output).getdata()
        index = 0
        print('[+] lsb start reading image')
        data = np.array(image)
        print(data)
        for i in range(len(data)):
            for j in range(len(data[0])):
                for k in range(len(data[0, 0])):
                    index += 1
                    number = data[i, j, k]
                    print(number, format(number, "08b"), format(number, "08b")[-1])
                    number = format(number, "08b")
                    self.message_b += number[-1]
                    if index > 2 * HEADER_SIZE:
                        return None

        message_lenght = int(self.message_b[:HEADER_SIZE], 2)
        print("final", self.message_b[:HEADER_SIZE], ".", self.message_b[HEADER_SIZE:message_lenght + HEADER_SIZE], ".",
              self.message_b[message_lenght + HEADER_SIZE:])

    print('[+] lsb end')


# Parameters from user
file_name = 'test.txt'
image_source = 'hs.jpeg'
image_output = 'out.jpeg'

# main
hide = Hide(file_name, image_source, image_output)
hide.encode()
dehide = Dehide(image_output)
dehide.dehide()
