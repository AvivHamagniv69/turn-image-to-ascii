#! /usr/bin/python3
from PIL import Image
from math import floor
import os
import sys

def main():
    if len(sys.argv) < 4:
        exit("please provide all arguments")

    # variables that are related to files/directories:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    all_files_in_folder = os.listdir(current_directory)
    
    if not os.path.exists(sys.argv[2]):
        file_path = current_directory+"/"+sys.argv[2]
        if sys.argv[2] not in all_files_in_folder:
            print("error file not found!")
            exit()
    
    else:
        file_path = sys.argv[2]

    im = Image.open(file_path)

    # variables that are related to the image:
    width_before_resize, height_before_resize = im.size
    ratio = width_before_resize/height_before_resize
    ratio = round(ratio)
    size = abs(int(sys.argv[1]))
    num_to_decide_ratio = 4

    # if the image ratio/2 is smaller then 1 then dividing it will just make it way bigger
    # so we need to handle that case for smaller images.
    if ratio/2 >= 1:
        num_to_decide_ratio = num_to_decide_ratio/(ratio/2)

    else:
        num_to_decide_ratio = num_to_decide_ratio/(ratio*2)

    new_im = im.resize((round(size*num_to_decide_ratio), round(size)))

    pix = new_im.load()

    file_of_ascii = open(sys.argv[3], "w")
    ascii_chars = ".,:;+*?%#@S"
    ascii_chars = list(ascii_chars)
    len_ascii = len(ascii_chars)
    width, height = new_im.size
    num_to_multiply = 1

    # we pass over the image before we draw the ascii image because otherwise it has a chance of going out of range
    for n in range(height):
        for i in range(width):
            pixelRGB = new_im.getpixel((i,n))
            if "(" not in str(pixelRGB):
                if floor(pixelRGB/(len_ascii*num_to_multiply)) >= len_ascii:
                    num_to_multiply = num_to_multiply+1
                    n = 0
                    i = 0

            else:
                r,g,b = pixelRGB
                brightness = (r+g+b)/3 

                if floor(brightness/(len_ascii*num_to_multiply)) >= len_ascii:
                    num_to_multiply = num_to_multiply+1
                    n = 0
                    i = 0

    for h in range(height):
            for row in range(width):
                pixelRGB = new_im.getpixel((row,h))
                # if there is only a brightness value and no RGB values we just use the brightness value
                if "(" not in str(pixelRGB):
                    ascii_to_write = ascii_chars[floor(pixelRGB/(len_ascii*num_to_multiply))]    
                    file_of_ascii.write(ascii_to_write)

                else:
                    r,g,b = pixelRGB
                    brightness = (r+g+b)/3 
                    ascii_to_write = ascii_chars[floor(brightness/(len_ascii*num_to_multiply))]
                    file_of_ascii.write(ascii_to_write)

            file_of_ascii.write("\n")

    file_of_ascii.close()

main()
