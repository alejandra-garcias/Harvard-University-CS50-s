'''In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.'''

import sys
from PIL import Image, ImageOps


def main():
    input,output = get_valid_filenames()
    #open Image
    try:
        image_file = Image.open(input)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    #shirt image:
    shirt = Image.open("shirt.png")
    #making shirt image the size
    size= shirt.size
    #resizing input:
    output_image  = ImageOps.fit(image_file,size)
    output_image.paste(shirt,shirt)
    #creating and saving it:
    output_image.save(output)


def get_valid_filenames():
    # Checks there's only one command-line argument
    if  len(sys.argv) == 3:
        #Makes sure that it is an image file
        if sys.argv[1].endswith(('.png', '.jpg', '.jpeg')) and sys.argv[2].endswith(('.png', '.jpg', '.jpeg')):
            if sys.argv[1][-4:].lower() == sys.argv[2][-4:].lower():
                return sys.argv[1:]
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid Input")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
