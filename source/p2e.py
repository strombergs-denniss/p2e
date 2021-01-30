import sys
import os
from setup import setup

arguments = sys.argv
action = arguments[len(arguments) - 1]
rootDirectory = os.getcwd() + '/'
setup = setup(rootDirectory)

if action == 'generate_values':
    from generate_values import generate_values
    generate_values(setup)
elif action == 'generate_images':
    from generate_images import generate_images
    generate_images(setup)
