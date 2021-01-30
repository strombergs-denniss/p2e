def setup(root_directory):
    return {
        'emote_image_directory': root_directory + 'data/emote_images/',
        'input_directory': root_directory + 'input/',
        'output_directory': root_directory + 'output/',
        'input': [
            {
                'file_name': 'ayaya.png',
                'image_size': (96, 96),
                'emote_size': (24, 24)
            }
        ]
    }
