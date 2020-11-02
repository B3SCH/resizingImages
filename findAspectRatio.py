import argparse
import os
from PIL import Image

def aspectRatio(tuple):
    return (tuple[0]/tuple[1])

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Find image aspect ratio")

    parser.add_argument('-d', '--directory', type=str, required=True,
                            help="Directory containing preprocessed images")

    args = parser.parse_args()
    directory = args.directory

    for img in os.listdir(directory):
        im = Image.open(directory + img)

        print("Image name: {}".format(im.filename))
        print("...dimensions: {}".format(im.size))

        print("...aspect ratio: {0:.2f}".format(aspectRatio(im.size)))
        print()
