import os
from PIL import Image
from math import sqrt

def generate_values(setup):
    emote_image_directory = setup['emote_image_directory']
    values = {}

    for file_name in os.listdir(emote_image_directory):
        image = Image.open(emote_image_directory + file_name).convert('RGB')
        width, height = image.size
        size = width * height
        total = [0, 0, 0]
        average = [0, 0, 0]

        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                total[0] += r
                total[1] += g
                total[2] += b

        average[0] = total[0] // size
        average[1] = total[1] // size
        average[2] = total[2] // size
        values[file_name] = average

    values_file = open('./values.py', 'w')
    values_file.write('values = ' + str(values) + '\n')
    values_file.close()
