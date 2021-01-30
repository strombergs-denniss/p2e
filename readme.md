# Pixels To Emotes

Small program which converts image pixels to emotes.

## Structure

1. All emote image are store in `/data/emote_images/`
2. All Emote URLs are store in `/data/emote_urls.txt`
3. You can configure settings in `/source/setup.py` file

## Usage

To generate values (in root directory):

    python ./source/p2e.py generate_values

To generate images (in root directory):

    python ./source/p2e.py generate_images

## Contribute

Currently the image generation is very slow so feel free to improve it, to contribute open pull request to master branch.
