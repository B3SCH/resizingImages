import argparse
import os
from PIL import Image

def resizeImage(image, MAX_SIZE):
    """
    Takes PIL.Image object and resizes according to optimal dimensions,
    returning resized PIL.Image

    PIL.Image --> PIL.Image
    """
    def aspectRatio(tuple):
        return (tuple[0]/tuple[1])

    def resizeRatio(int):
        return (MAX_SIZE[int]/image.size[int])

    def optimalImageSize(r):
        optWidth = int(r * image.size[0])
        optHeight = int(r * image.size[1])
        return (optWidth, optHeight)

    if (aspectRatio(image.size) > aspectRatio(MAX_SIZE)):
        r = resizeRatio(0) # numerator (width) greater
    elif (aspectRatio(image.size) < aspectRatio(MAX_SIZE)):
        r = resizeRatio(1) # denominator (height) greater

    optSize = optimalImageSize(r)
    resizedImage = image.resize(size=optSize)

    return resizedImage

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Rescale images")

    parser.add_argument('-d', '--directory', type=str,
                        required=False, help='Directory containing the images')

    parser.add_argument('-i', '--image', type=str,
                        required=False, help='Name of image file')

    # THIS MAY NEED WORK -- add as a default?
    parser.add_argument('-s', '--size', type=int, nargs=2,
                        required=True, metavar=('width', 'height'),
                        help='Image size, tuple: (width, height)')

    args = parser.parse_args()

    # define arguments
    IMAGE = args.image
    print("args.image type: ", type(IMAGE))
    print("args.image value: ", IMAGE)
    MAX_SIZE = args.size
    print("args.size type: ", type(MAX_SIZE))
    print("args.image value: ", MAX_SIZE)

    # HERE ON DOWN, VARIABLE NAMES WILL NEED TO BE REWRITTEN
    # this should happen within a for loop for images in dictionary
    im = Image.open(IMAGE)

    print("Image name: {}".format(im.filename))
    print("Image dimensions: {}".format(im.size))

    if (im.size[0] <= MAX_SIZE[0]) and (im.size[1] <= MAX_SIZE[1]):
        print("Image dimensions are fine")

    if (im.size[0] > MAX_SIZE[0]) or (im.size[1] > MAX_SIZE[1]):
        print("Image dimensions will need to be resized")
        print("Entering resizing function...")
        resizedImage = resizeImage(im, MAX_SIZE)
        print("Resized image dimensions: {}".format(resizedImage.size))
