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
        image = Image.open(self.image_source)
        data = np.array(image)
        self.message_b = ''.join([format(i, "08b") for i in self.message_b])
        # header = format(len(self.message_b), "08b")
        header = '{:032b}'.format(len(self.message_b))
        self.message_b = header + self.message_b

        def hide(data):
            index = 0
            for i in range(len(data)):
                for j in range(len(data[0])):
                    for k in range(len(data[0, 0])):
                        var = format(data[i, j, k], "08b")
                        var = var[:-1] + str(self.message_b[index])
                        index += 1
                        var = int(var, 2)
                        data[i, j, k] = var
                        if index == len(self.message_b):
                            return None

        hide(data)
        im = Image.fromarray(data)
        im.save(self.image_output)


class Dehide():
    def __init__(self, image_output):
        self.image_output = image_output
        self.message_b = ''

    def dehide(self):
        image = Image.open(self.image_output)
        index = 0
        data = np.array(image)
        for i in range(len(data)):
            for j in range(len(data[0])):
                for k in range(len(data[0, 0])):
                    index += 1
                    number = data[i, j, k]
                    number = format(number, "08b")
                    self.message_b += number[-1]
                    if index > 2 * HEADER_SIZE:
                        return None

    def result(self):
        message_lenght = int(self.message_b[:HEADER_SIZE], 2)
        header = self.message_b[:HEADER_SIZE]
        body = self.message_b[HEADER_SIZE:message_lenght + HEADER_SIZE]
        return body


# main
def main():
    # Parameters from user
    file_name = 'test.txt'
    image_source = 'test.png'
    image_output = 'out.png'
    print("[+] LSB STENOGRAPHY TOOL OF A VERY HIGH STANDING")
    print("1 - Write hidden data to image ")
    print("2 - Read hidden data from image")
    choice = int(input("Enter your option : "))
    if choice == 1:
        print('[+] Hiding data ...')
        hide = Hide(file_name, image_source, image_output)
        hide.encode()
        print('[+] Finish writing data to image')
    elif choice == 2:
        print('[+] Reading data ...')
        dehide = Dehide(image_output)
        dehide.dehide()
        data = dehide.result()
        print('[+] Finish reading data from image')

        def bitstring_to_bytes(s):
            v = int(s, 2)
            b = bytearray()
            while v:
                b.append(v & 0xff)
                v >>= 8
            return bytes(b[::-1])
        data = bitstring_to_bytes(data)
        open("out.txt", "wb").write(data)
        print('[+] Finish writing data to file')
        print(open("out.txt", "r").read())

main()