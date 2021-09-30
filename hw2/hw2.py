# Author: Bobby Davis
# Purpose: The following program take a list of images of the exact same
#          location at differnt times and uses a median filter to create 
#          a new image with undesired objects removed. List of images to
#          be filtered should be an odd number.

from PIL import Image
import glob

def median(target_list):    # find median of an odd numbered list
    list_length = len(target_list)
    target_list.sort()
    index = list_length // 2
    result = target_list[index]
    return result

image_files = []    # list to hold all images

# get all files with .png extention and add them to list
for image in glob.glob('hw2_images/*.png'):
    image_files.append(Image.open(image))

def filter_images(image_list):
    # get image dimensions and create blank canvas of appropriate size
    w, h = image_list[0].width, image_list[0].height
    canvas = Image.new('RGB', (w, h))

    red_pixels = []     # holds red channel values for current pixel location
    green_pixels = []   # holds green channel values for current pixel location
    blue_pixels = []    # holds blue channel values for current pixel location

    x, y = 0, 0 # set initial pixel corrdinates

    for x in range(w):  # iterate through rows (x-axis)
        for y in range(h):  # iterate through columns (y-axis)
            for i in image_list:   # iterate through list of images
                current_tup = i.getpixel((x, y))    # get current (r,g,b) tuple
                red_pixels.append(current_tup[0])   # save current red channel value
                green_pixels.append(current_tup[1]) # save current green channel value
                blue_pixels.append(current_tup[2])  # save current blue channel value
            r = median(red_pixels)      # find median of red channel values
            g = median(green_pixels)    # find median of green channel values
            b = median(blue_pixels)     # find median of blue channel values
            canvas.putpixel((x, y), (r, g, b))  # write new pixel to canvas
            # clear all channel lists for current pixel
            red_pixels.clear()
            green_pixels.clear()
            blue_pixels.clear()

    return canvas

new_image = filter_images(image_files)
new_image.show()   # show new image
new_image.save('result.png')   # save new image