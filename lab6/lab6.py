# Bobby Davis
# Lab 6

from PIL import Image
import numpy as np

# Image setup
im1 = Image.open('sunset.jpg')
im2 = Image.open('jeanne_small.jpg')
im3 = Image.open('hamburg.jpg')

image_list = [im1, im2, im3]    # list to hold opened images

# TASK 1 - SUNSET FILTER
im1.show()  # open original image for comparison

def reduce_green_blue(picture, percent):    # function to reduce green and blue channels by given percentage
    percent_as_decimal = percent/100    # convert percentage to decimal
    new_list=[] # list to store new pixel values

    for p in picture.getdata(): # iterate through flatlist of pixels
        new_list.append((p[0], p[1]-int(p[1]*percent_as_decimal), p[2]-int(p[2]*percent_as_decimal)))   # reduce green and blue channels and add new pixel to list

    picture.putdata(new_list)   # paint new picture using reduced pixel values
    picture.show()  # display modified image
    picture.save('new_sunset.png')  # save modified image

# call function to reduce green and blue channels by 30%
reduce_green_blue(im1, 30)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TASK 2 - COLLAGE
canvas_width = 0
max_height = 0

# iterate through list of images to find max height and sum of widths
for i in image_list:
    canvas_width += i.width
    if i.height > max_height:
        max_height = i.height

canvas = Image.new('RGB', (canvas_width + 40, max_height))  # create new canvas with appropriate dimensions; + 40 to width to make room for space between images

last_x = 0  # Keep track of last pixel drawn on x-axis

def copy_image(img, x): # copies an image to main; images will be added horizontally across the x-axis
    w,h = img.width, img.height # get dimensions for current image to be added

    # target varibles are the position where pixels will be copied to canvas
    target_x = x + 10   # add 10 pixels to create space
    for source_x in range(0, img.width):    # iterate through pixels on x-axis
        target_y = 0
        for source_y in range(0, img.height):   # iterate through pixels on y-axis 
            pixel = img.getpixel((source_x, source_y))
            canvas.putpixel((target_x, target_y), pixel)
            target_y += 1
        target_x += 1

    return target_x # return last pixel position on x-axis

# call function to copy images over to canvas
last_x = copy_image(im1, last_x)
last_x = copy_image(im2, last_x)
last_x = copy_image(im3, last_x)

canvas.show()   # display result image
canvas.save('collage.png')   # save result image