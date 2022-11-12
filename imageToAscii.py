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
-flat makes the ascii drawing only with ":" and " ", removing detail but easier on the eyes

-h for help''')

    # we dont want the - in the start of the commands
    for removing in range(len(sys.argv)):
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
    file_of_ascii = open(sys.argv[3], "w")
    
    ascii_chars = ".,:;+*?%#@S"
    ascii_chars = list(ascii_chars)
    
    width, height = new_im.size
    numbers_for_ascii = [0]
    # we make an array between 0 and 255 with the difference between each numbers is 255 divided by the length of the ascii table
    for numbers in range(len(ascii_chars)):
        numbers_for_ascii.append((255/len(ascii_chars))+(numbers_for_ascii[numbers]))

    if "flat" in sys.argv:
        biggest_num = 1
        for n in range(height):
            for i in range(width):
                brightness = new_im.getpixel((i,n))
                if brightness > biggest_num:
                    biggest_num = brightness
    
    for h in range(height):
        for row in range(width):
            brightness = new_im.getpixel((row,h))
            if "flat" in sys.argv:
                if brightness >= biggest_num/2:
                    file_of_ascii.write(":")
                    continue
                
                else:
                    file_of_ascii.write(" ")
                    continue
            
            numbers_for_ascii.append(brightness)
            numbers_for_ascii.sort()
            num_before_brightness = numbers_for_ascii[(numbers_for_ascii.index(brightness)-1)]
            num_after_brightness = numbers_for_ascii[(numbers_for_ascii.index(brightness)-1)]

            # we want to use the array afterwerds so we cant jus leave that number in there
            del numbers_for_ascii[numbers_for_ascii.index(brightness)]
            # these 2 statments find out which cell the brightness value is closer to.
            if num_after_brightness-brightness < num_before_brightness-brightness and brightness <= 255:
                file_of_ascii.write(ascii_chars[numbers_for_ascii.index(num_after_brightness)])

            elif brightness != 0:
                file_of_ascii.write(ascii_chars[numbers_for_ascii.index(num_before_brightness)])

        file_of_ascii.write("\n")

    if "print" in sys.argv:
        with open(sys.argv[3], "r") as foa:
            print(foa.read())

    file_of_ascii.close()
    im.close()

main()
