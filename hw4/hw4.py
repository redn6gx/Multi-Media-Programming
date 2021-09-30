# HEADER
    # Bobby Davis
    # 4/16/2021
    # CST 205
    # Description: This file serves as the main control center for the backend where routes are defined.
    #              Variables sent to and from rendered html pages are directed through here as well.

# IMPORTS
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from image_info import image_info
from PIL import Image
import random

# create an insatance of Flask
app = Flask(__name__)
bootstrap = Bootstrap(app)

# VIEW FUNCTIONS / ROUTE DECORATORS
@app.route('/')
def home():
    random.shuffle(image_info)
    return render_template('index.html', img1 = image_info[0], img2 = image_info[1], img3 = image_info[2])

@app.route('/picture/<pic_id>')
def display_img(pic_id):
    # find the image that was selected from the homepage in the image_info list then extract the image information with PILLOW
    for img in image_info:
        if img['id'] == pic_id:
            im = Image.open('static/images/' + pic_id + '.jpg')
            title = img['title']
            author = img['flickr_user']
            mode = im.mode
            width = im.width
            height = im.height
            img_format = im.format
            break
    return render_template('picture.html', pic_id = pic_id, pic_title = title, img_title = title, 
                img_author = author, img_mode = mode, img_width = width, img_height = height, img_format = img_format)
