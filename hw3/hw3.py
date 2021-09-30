# HOMEWORK #3

# Bobby Davis
# 3/17/21
# CST 205
# Program Description: This program displays a GUI for a user to interact with.
#                      If the user enters keywords or phrases the program will try to find a photo
#                      that that matches the user input. If no matches are found then an appropriate
#                      message is displayed to inform the user. The user can also select from a variety
#                      of photo filtering and editing options to apply before clicking search. All functions
#                      with the exception of thumbnail() repaint over the old picture but are not saved and do
#                      not overwrite the old picture.

# IMPORTS
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox, QLineEdit
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from image_info import image_info
from PIL import Image

match_record = [] # Holds the number of matches for each image at it's corresponding index

# class for user interface photo editor/search engine
class SearchInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.option_label = QLabel('Photo Options')
        self.img_options_list = ['None', 'Sepia', 'Negative', 'Grayscale', 'Thumbnail'] # create List of Photo Options
        self.combo = QComboBox()    # create dropdown menu
        self.combo.addItems(self.img_options_list) # populate dropddown with options

        self.search_label = QLabel('Search for Picture!')
        self.srch_box = QLineEdit() # user input field

        self.srch_btn = QPushButton("Search")

        # Create U.I. Layout (widgets will appear in order added)
        vbox = QVBoxLayout()
        vbox.addWidget(self.option_label)
        vbox.addWidget(self.combo)
        vbox.addWidget(self.search_label)
        vbox.addWidget(self.srch_box)
        vbox.addWidget(self.srch_btn)
        self.setLayout(vbox)    # apply vbox layout

        # Listeners
        self.srch_btn.clicked.connect(self.find_match)

    # function that finds a photo with the most matches and applys filter if selected
    @Slot()
    def find_match(self):
        max_matches = 0 # keeps track of highest match count
        curr_matches = 0 # keeps track of match count for current image
        result_index = 0 # will store index of image with most matches here
        
        for i, img in enumerate(image_info):    # itereate through images
            if self.srch_box.text().lower().__contains__(img['title'].lower()): # check for matching title
                curr_matches = curr_matches + 1
            for tag in img['tags']: # iterate through tags of an image
                if self.srch_box.text().lower().__contains__(tag.lower()):  # check for matching tags
                    curr_matches = curr_matches + 1
            
            if curr_matches > max_matches:  # check if a bigger match count has been found
                result_index = i    # save new index of image with most matches
                max_matches = curr_matches  # save new max match count

            match_record.append(curr_matches) # add the number of matches for an image to the record
            curr_matches = 0 # reset match counter

        print(f"Number of Matches for Each Image by Index: {match_record}")

        # if no matches were found for any image then inform the user with a pop-up window
        if(max_matches == 0):
            self.new_window = ErrorWindow() # create new ErrorWindow object
            self.new_window.show()  # display ErrorWindow
            return

        print(f"Max Match Count: {max_matches}")
        print(f"Image Info: {image_info[result_index]}\n")

        img_id = image_info[result_index]['id']
        path = 'hw3_images' + "/" + img_id + '.jpg' # create path to image file
        retrieved_img = Image.open(path)

        # get the selected filter/edit option from the dropdown menu and call function accordingly
        combo_index = self.combo.currentIndex()
        if(self.img_options_list[combo_index] == "Sepia"):
            sepia(retrieved_img)
        elif(self.img_options_list[combo_index] == "Negative"):
            negative(retrieved_img)
        elif(self.img_options_list[combo_index] == "Grayscale"):
            grayscale(retrieved_img)
        elif(self.img_options_list[combo_index] == "Thumbnail"):
            thumbnail(retrieved_img, 3)
        else:
            retrieved_img.show()    # Display unedited image

        match_record.clear() # Clear match record for next search

# class to define error window pop-up
class ErrorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Background')
        p = self.palette()
        p.setColor(self.backgroundRole(), 'red')
        self.setPalette(p)
        self.message_label = QLabel('Sorry, but we couldn\'t find any pictures that matched your search :(')

        vbox = QVBoxLayout()
        vbox.addWidget(self.message_label)
        self.setLayout(vbox)

# FUNCTIONS FOR EDITING PHOTO
def sepia(img): # applys a sepia filter
    img_list = img.getdata()
    sepia_list = map(sepia_pixel, img_list)    # map new pixel value returned from sepia_pixel() to old pixel position
    img.putdata(list(sepia_list))
    img.show()

# sepia function's helper method
def sepia_pixel(pixel): # modifies a pixel color based on the red channel value
    if pixel[0] < 100:
        r,g,b = int(pixel[0]*1.1), pixel[1], int(pixel[2]*.9)
    elif pixel[0] > 62 and pixel[0]<192:
        r,g,b = int(pixel[0]*1.15), pixel[1], int(pixel[2]*.85)
    else:
        r = int(pixel[0]*1.08)
        if r>=255: r=130
        g,b = pixel[1], pixel[2]//2  
    return r,g,b

def negative(img):  # applys a negative filter
    pixel_list = img.getdata()
    new_list=[] # list to store new pixel values

    for p in img.getdata(): # iterate through flatlist of pixels
        new_list.append((255-p[0], 255-p[1], 255-p[2]))

    img.putdata(new_list)
    img.show()

def grayscale(img): # applys a gray filter
    pixel_list = img.getdata()
    new_list = []

    for p in img.getdata(): # iterate through flatlist of pixels
        average = (p[0] + p[1] + p[2])//3
        new_list.append((average, average, average))

    img.putdata(new_list)
    img.show()

def thumbnail(img, shrink_factor):  # shrinks picture
    w,h = img.width, img.height # get image dimensions
    canvas = Image.new('RGB', ((w//shrink_factor)+1,(h//shrink_factor)+1))  # make new canvas appropriate for smaller picture size

    # iterate through image pixels, left to right, column by column, skipping pixels by the shrink factor
    for trg_x, src_x in enumerate(range(0, w, shrink_factor)):
        for trg_y, src_y in enumerate(range(0, h, shrink_factor)):
            px = img.getpixel((src_x, src_y))   # get pixel at current position
            canvas.putpixel((trg_x, trg_y), px) # add pixel to canvas

    canvas.show()

# Initalize and Run application
app = QApplication(sys.argv)
main = SearchInterface()
main.show()
sys.exit(app.exec_())
