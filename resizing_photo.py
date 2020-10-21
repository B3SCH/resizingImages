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
        """
        tuple --> float
        """
        return (tuple[0]/tuple[1])

    def resizeRatio(int):
        """
        int --> float
        """
        return (MAX_SIZE[int]/image.size[int])

    def optimalImageSize(r):
        """
        float --> tuple
        """
        optWidth = int(r * image.size[0])
        optHeight = int(r * image.size[1])
        return (optWidth, optHeight)

    if (aspectRatio(image.size) > aspectRatio(MAX_SIZE)):
        r = resizeRatio(0) # numerator (width) greater
    elif (aspectRatio(image.size) < aspectRatio(MAX_SIZE)):
        r = resizeRatio(1) # denominator (height) greater

    optSize = optimalImageSize(r)
    resizedImage = image.resize(size=optSize)

    resizedImage.filename = image.filename

    return resizedImage

def saveImageToDirectory(image, directory):
    """
    (PIL.Image, str) --> None
    """
    def checkDir(directory):
        return os.path.isdir(directory)

    def writeFileName(fileName):
        splitName = fileName.split('/')
        outfileName = 'POST_' + splitName[1]
        return outfileName

    if checkDir(directory) == False:
        os.mkdir(directory)

    outfileName = directory + writeFileName(image.filename)
    image.save(outfileName)

    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Rescale images")

    parser.add_argument('-d', '--in_directory', type=str, required=True,
                            help='Directory containing preprocessed images')

    parser.add_argument('-o', '--out_directory', type=str, required=True,
                        help='Directory containing postprocessed images')

    parser.add_argument('-i', '--image', type=str, required=False,
                        help='Name of image file')

    # THIS MAY NEED WORK -- add default values?
    parser.add_argument('-s', '--size', type=int, nargs=2,
                        required=True, metavar=('width', 'height'),
                        help='Image size, tuple: (width, height)')

    args = parser.parse_args()

    # define arguments
    MAX_SIZE = args.size
    IN_DIRECTORY = args.in_directory
    OUT_DIRECTORY = args.out_directory

    for img in os.listdir(IN_DIRECTORY):
        im = Image.open(IN_DIRECTORY + img)

        print("Image name: {}".format(im.filename))
        print("Image dimensions: {}".format(im.size))

        if (im.size[0] <= MAX_SIZE[0]) and (im.size[1] <= MAX_SIZE[1]):
            print("Image dimensions are fine")
            saveImageToDirectory(im, OUT_DIRECTORY)

        if (im.size[0] > MAX_SIZE[0]) or (im.size[1] > MAX_SIZE[1]):
            #print("Image dimensions will need to be resized")
            #print("Entering resizing function...")
            imResized = resizeImage(im, MAX_SIZE)
            print("New image name: {}".format(imResized.filename))
            print("New image dimensions: {}".format(imResized.size))
            #print("Resized image dimensions: {}".format(resizedImage.size))
            saveImageToDirectory(imResized, OUT_DIRECTORY)
