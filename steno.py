import numpy as np
from PIL import Image
from termcolor import colored

def decode_image():
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


def message(mot):
    # start_time = time.time()
    for n in range(len(file_data)):

        # print("--- %s seconds ---" % (time.time() - start_time))
        if n < len(mot):
            # new_file_data.append(ord(mon[n]))
            new_file_data.append(format((ord(mot[n])), "b"))
        else:
            new_file_data.append(file_data[n])

    # print(new_file_data)
    print("Message inscrit")

mot = 'test'
source = 'IMG_7834.jpeg'
image = Image.open(source, 'r')
file_data = []
new_file_data = []
width, height = image.size

print(width, height)

print('[+] lsb start')

pixels = np.array(image)

# decode_image(file_data,pixels)
# message(mot)
print(mot)
data = []
for x in range(len(mot)):
    data = [((ord(mot[x])), "08b"), ord(mot[x])]
print(data)
