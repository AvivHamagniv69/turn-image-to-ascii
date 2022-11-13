#! /usr/bin/python3
from PIL import Image

# from math import floor
import os
import argparse


def get_args():
    parser = argparse.ArgumentParser("turn image to ascii")
    parser.add_argument("-size", type=int, default=50, help="Size of the ascii image")
    parser.add_argument(
        "-print",
        type=bool,
        default=False,
        help="Choose if to print the file to the terminal",
    )
    parser.add_argument(
        "-input", type=str, default="should_exit", help="Path to input image"
    )
    parser.add_argument(
        "-output", type=str, default="ascii.txt", help="Path to output text file"
    )
    parser.add_argument(
        "-mode",
        type=str,
        default="simple",
        choices=["simple", "flat"],
        help="basic ascii table, 2 characters that create a flat image",
    )
    parser.add_argument(
        "-add_ascii_table",
        type=str,
        default=".,:;+*?%#@S",
        help="add your own ascii table",
    )

    args = parser.parse_args()
    return args


def mode_flat(height: int, width: int, new_im: Image.Image, file_of_ascii):
    # this loop finds the pixel with the highest brightness value, the reason we need this is for very dark images it would barely draw any ":" because it would only draw them if the pixel is above 255/2, so now it is proportional to the image.
    # if argus.mode == "flat":
    biggest_num = 1
    for n in range(height):
        for i in range(width):
            brightness = new_im.getpixel((i, n))
            if brightness > biggest_num:
                biggest_num = brightness

    for h in range(height):
        for row in range(width):
            brightness = new_im.getpixel((row, h))
            # if argus.mode == "flat":
            if brightness >= biggest_num / 2:
                file_of_ascii.write(":")
                # continue
            else:
                file_of_ascii.write(" ")
                # continue
        file_of_ascii.write("\n")
    return file_of_ascii


def mode_simple(height: int, width: int, new_im: Image.Image, file_of_ascii):
    ascii_chars = argus.add_ascii_table
    ascii_chars = list(ascii_chars)

    # width, height = new_im.size
    numbers_for_ascii = [0]
    # we make an array between 0 and 255 with the difference between each numbers is 255 divided by the length of the ascii table.
    for numbers in range(len(ascii_chars)):
        numbers_for_ascii.append(
            (255 / len(ascii_chars)) + (numbers_for_ascii[numbers])
        )
    for h in range(height):
        for row in range(width):
            brightness = new_im.getpixel((row, h))
            numbers_for_ascii.append(brightness)
            numbers_for_ascii.sort()
            num_before_brightness = numbers_for_ascii[
                (numbers_for_ascii.index(brightness) - 1)
            ]
            num_after_brightness = numbers_for_ascii[
                (numbers_for_ascii.index(brightness) - 1)
            ]

            # we want to use the array afterwerds so we cant jus leave that number in there.
            del numbers_for_ascii[numbers_for_ascii.index(brightness)]
            # these 2 statments find out which cell the brightness value is closer to.
            if (
                num_after_brightness - brightness < num_before_brightness - brightness and brightness <= 255
            ):
                file_of_ascii.write(
                    ascii_chars[numbers_for_ascii.index(num_after_brightness)]
                )

            # since we know from the previous statment that brightness isn't close to num_after_brightness we only need to verify that brightness != 0 or it goes out of range.
            elif brightness != 0:
                file_of_ascii.write(
                    ascii_chars[numbers_for_ascii.index(num_before_brightness)]
                )

            else:
                file_of_ascii.write(ascii_chars[0])
        file_of_ascii.write("\n")
    return file_of_ascii


def main(argus):
    # no image input was provided so we simply exit
    if argus.input == "should_exit":
        exit("please provide all arguments or write -h for help")

    # variables that are related to files/directories:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    all_files_in_folder = os.listdir(current_directory)

    # checks if the file exists
    if not os.path.exists(argus.input):
        file_path = current_directory + "/" + argus.input
        if argus.mode not in all_files_in_folder:
            print("error file not found!")
            exit()

    else:
        file_path = argus.input

    im = Image.open(file_path).convert("L")

    # variables that are related to the image:
    width_before_resize, height_before_resize = im.size
    ratio = width_before_resize / height_before_resize
    ratio = round(ratio)
    size = argus.size
    # if we resize an image with an aspect ratio of 2 with the number 4 it preserves the aspect ratio of the image.
    num_to_decide_ratio = 4

    # if the image ratio/2 is smaller then 1 then dividing it will just make it way bigger.
    # so we need to handle that case for smaller images.
    if ratio / 2 >= 1:
        # the formula for preserving the aspect ratio for the image, for example 4/(2/2) = 4 this is for an aspect ratio of 2 which preserves it.
        num_to_decide_ratio = num_to_decide_ratio / (ratio / 2)

    else:
        # if the aspect ratio is smaller then one then dividing it will make the math wrong so we have this statement.
        num_to_decide_ratio = num_to_decide_ratio / (ratio * 2)

    new_im = im.resize((round(size * num_to_decide_ratio), round(size)))

    try:
        file_of_ascii = open(argus.output, "w")
    except Exception:
        raise Exception("invalid path or gave a directory")

    width, height = new_im.size
    # this loop finds the pixel with the highest brightness value, the reason we need this is for very dark images it would barely draw any ":" because it would only draw them if the pixel is above 255/2, so now it is proportional to the image.
    if argus.mode == "flat":
        file_of_ascii = mode_flat(height, width, new_im, file_of_ascii)
    else:
        file_of_ascii = mode_simple(height, width, new_im, file_of_ascii)
    #     biggest_num = 1
    #     for n in range(height):
    #         for i in range(width):
    #             brightness = new_im.getpixel((i,n))
    #             if brightness > biggest_num:
    #                 biggest_num = brightness

    # for h in range(height):
    #     for row in range(width):
    #         brightness = new_im.getpixel((row,h))
    #         if argus.mode == "flat":
    #             if brightness >= biggest_num/2:
    #                 file_of_ascii.write(":")
    #                 continue

    #             else:
    #                 file_of_ascii.write(" ")
    #                 continue

    #         numbers_for_ascii.append(brightness)
    #         numbers_for_ascii.sort()
    #         num_before_brightness = numbers_for_ascii[(numbers_for_ascii.index(brightness)-1)]
    #         num_after_brightness = numbers_for_ascii[(numbers_for_ascii.index(brightness)-1)]

    #         # we want to use the array afterwerds so we cant jus leave that number in there.
    #         del numbers_for_ascii[numbers_for_ascii.index(brightness)]
    #         # these 2 statments find out which cell the brightness value is closer to.
    #         if num_after_brightness-brightness < num_before_brightness-brightness and brightness <= 255:
    #             file_of_ascii.write(ascii_chars[numbers_for_ascii.index(num_after_brightness)])

    #         # since we know from the previous statment that brightness isn't close to num_after_brightness we only need to verify that brightness != 0 or it goes out of range.
    #         elif brightness != 0:
    #             file_of_ascii.write(ascii_chars[numbers_for_ascii.index(num_before_brightness)])

    #         else:
    #             file_of_ascii.write(ascii_chars[0])

    #     file_of_ascii.write("\n")

    if argus.print:
        with open(argus.output, "r") as foa:
            print(foa.read())

    file_of_ascii.close()
    im.close()


if "__main__" == __name__:
    argus = get_args()
    main(argus)
