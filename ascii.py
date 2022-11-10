#! /usr/bin/python3
from PIL import Image
from math import floor
import os
import sys

def main():
    if sys.argv[1] == "-h":
        exit('''-num size of image (25 for example)

-/optional_path/image.image_format full path to the image we transform (if full path not specified it will use current directory instead)

-/optional_path/ascii.txt full path to where we put the ascii text file (if full path not specified will use full directory instead)

-print (optional) argument is which prints the file to the terminal

-simple uses a smaller ascii table (".,:;+*?%#@)
-complex uses a bigger ascii table ($@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,\"^`'. )
-flat makes the ascii drawing only with ":" and " ", removing detail but easier on the eyes

-h for help''')

    # we dont want the - in the start of the commands
    lensys = len(sys.argv)
    for removing in range(lensys):
        sys.argv[removing] = sys.argv[removing].replace('-', '', 1)

    if len(sys.argv) < 4:
        exit("please provide all arguments or write -h for help")

    # variables that are related to files/directories:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    all_files_in_folder = os.listdir(current_directory)
    
    # checks if the file exists
    if not os.path.exists(sys.argv[2]):
        file_path = current_directory+"/"+sys.argv[2]
        if sys.argv[2] not in all_files_in_folder:
            print("error file not found!")
            exit()
    
    else:
        file_path = sys.argv[2]

    im = Image.open(file_path).convert('L')

    # variables that are related to the image:
    width_before_resize, height_before_resize = im.size
    ratio = width_before_resize/height_before_resize
    ratio = round(ratio)
    size = abs(int(sys.argv[1]))
    # if we resize an image with an aspect ratio of 2 with the number 4 it preserves the aspect ratio of the image
    num_to_decide_ratio = 4

    # if the image ratio/2 is smaller then 1 then dividing it will just make it way bigger
    # so we need to handle that case for smaller images.
    if ratio/2 >= 1:
        # the formula for preserving the aspect ratio for the image, for example 4/(2/2) = 4 this is for an aspect ratio of 2 which preserves it.
        num_to_decide_ratio = num_to_decide_ratio/(ratio/2)

    else:
        # if the aspect ratio is smaller then one then dividing it will make the math wrong so we have this statement
        num_to_decide_ratio = num_to_decide_ratio/(ratio*2)

    new_im = im.resize((round(size*num_to_decide_ratio), round(size)))
    pix = new_im.load()
    file_of_ascii = open(sys.argv[3], "w")
    
    # since simple is the default value its activated both if its specified and if its not
    if "simple" in sys.argv or "simple" and "complex" not in sys.argv:
        ascii_chars = ".,:;+*?%#@S"
        ascii_chars = list(ascii_chars)
        len_ascii = len(ascii_chars)
        
    else:
        ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,\"^`'. "
        ascii_chars = list(ascii_chars)
        ascii_chars.reverse()
        len_ascii = len(ascii_chars)
    
    width, height = new_im.size
    num_to_multiply = 1

    # we pass over the image before we draw the ascii image because otherwise it has a chance of going out of range
    for n in range(height):
        # if we chose the flat option there is no need to choose from an ascii table because its 2 characters so this loop is uneeded
        if "flat" in sys.argv:
            break

        for i in range(width):
            brightness = new_im.getpixel((i,n))
            if floor(brightness/(len_ascii*num_to_multiply)) >= len_ascii:
                num_to_multiply = num_to_multiply+1
                n = 0
                i = 0
    
    for h in range(height):
        for row in range(width):
            brightness = new_im.getpixel((row,h))
            if "flat" in sys.argv:
                if brightness >= 127.5:
                    file_of_ascii.write(":")
                    continue
                
                else:
                    file_of_ascii.write(" ")
                    continue

            ascii_to_write = ascii_chars[floor(brightness/(len_ascii*num_to_multiply))]    
            file_of_ascii.write(ascii_to_write)

        file_of_ascii.write("\n")

    # currently dosent work, why? good question, i promise to solve it though
    if "print" in sys.argv:
        with open(sys.argv[3], "r") as foa:
            print(foa.read())
            print('\n')

    file_of_ascii.close()

main()
