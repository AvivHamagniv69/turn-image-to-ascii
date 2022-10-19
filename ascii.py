from PIL import ImageTk, Image
from PIL import *
from math import floor

file_path = input("enter file path: ")
im = Image.open(file_path)

width1, height1 = im.size
ratio = width1/height1
ratio = round(ratio)
print(ratio)
size = int(input("enter the size of image (ratio will be kept)"))
new_im = im.resize((round(size*4), round(size)))
print(new_im.size)

pix = new_im.load()

file_of_ascii = open("ascii_art.txt", "w")
ascii_chars = ".,:;+*?%#@S"
ascii_chars = list(ascii_chars)
len_ascii = len(ascii_chars)
print(ascii_chars)
width, height = new_im.size
arr = []
num_to_multiply = 1

for h in range(height):
    try:
        for row in range(width):
            pixelRGB = new_im.getpixel((row,h))
            r,g,b = pixelRGB
            brightness = (r+g+b)/3 
            ascii_to_write = ascii_chars[floor(brightness/(len_ascii*num_to_multiply))]

            file_of_ascii.write(ascii_to_write)
        file_of_ascii.write("\n")

    except:
        num_to_multiply = num_to_multiply+1
        row = row - 1
        file_of_ascii.write("\n")

file_of_ascii.close()
