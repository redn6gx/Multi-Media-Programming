# Program prompts user to input the name of a .txt file that contains the pixel values and then converts it into a picture.
# Program then prompts the user to input the name they would like to save the picture as.
# .txt file should be in the same directory as this program

from PIL import Image

read_lines = [] # list/matrix to store pixel values

txt_file = input('Enter the name of the .txt file that conatins pixel values. (include file extention):\n')  # Prompt user to type .txt file name

with open(txt_file, 'r') as f:    # open lisa.txt file with all the pixel values in it
    line_list = f.readlines()   # read each line of the lisa.txt file into one list

print('\nUNSPLIT DATA:')
print(line_list, '\n')

for i, line in enumerate(line_list):
    read_lines.append(line.split()) # split each line into its own list and add it to read_lines list

width = 0   # assume max width is zero
height = len(read_lines)    # set height to length of read_lines list (number of lines/lists)

print('SPLIT DATA:')
for i, line in enumerate(read_lines):
    read_lines[i][-1] = read_lines[i][-1][:-1]  # slices the last character (;) off the last element in a list
    print(read_lines[i])
    if(len(line) > width):  # find max width (longest list in  read_lines)
        width = len(line)

print('\nCanvas Size')
print(f'width = {width}, height = {height}')

canvas = Image.new('L', (width, height))    # create blank canvas with appropriate width and hieght values

for x in range(width):
    for y in range(height):
        canvas.putpixel((x,y), int(read_lines[y][x]))  # add pixels from read_lines matrix to the canvas column by column

result = input('\nEnter the name you would like to save the picture as. (include file extention appropriate for images; png, jpg, bmp, etc.):\n')   # prompt user to type the name they would like to save the file as.
canvas.save(result)

print(f'\n{txt_file} saved as {result}')

canvas.show() # open and display image