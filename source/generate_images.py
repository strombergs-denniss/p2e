import os
from PIL import Image
from math import sqrt
from values import values

def generate_images(setup):
    input_directory = setup['input_directory']
    output_directory = setup['output_directory']
    emote_image_directory = setup['emote_image_directory']
    input = setup['input']

    for file in input:
        file_name = file['file_name']
        image_size = file['image_size']
        emote_size = file['emote_size']
        image = Image.open(input_directory + file_name).convert('RGB').resize(image_size)

        width, height = image.size
        file_names = []

        for x in range(width):
            strip = []

            for y in range(height):
                r, g, b = image.getpixel((x, y))
                closest_key = ''
                closest_value = float('inf')

                for key in values:
                    r2, g2, b2 = values[key]
                    distance = (r - r2) ** 2 + (g - g2) ** 2 + (b - b2) ** 2

                    if distance < closest_value:
                        closest_value = distance
                        closest_key = key

                strip.append(closest_key)
            file_names.append(strip)

        total_width = width * emote_size[0]
        total_height = height * emote_size[1]
        output = Image.new('RGB', (total_width, total_height))

        for x in range(len(file_names)):
            strip = file_names[x]

            for y in range(len(strip)):
                file_name = strip[y]
                image = Image.open(emote_image_directory + file_name).convert('RGB').resize(emote_size)
                output.paste(image, (x * emote_size[0], y * emote_size[1]))

        output.save(output_directory + file['file_name'])
