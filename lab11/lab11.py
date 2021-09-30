from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# creat an insatance of Flask
app = Flask(__name__)
bootstrap = Bootstrap(app) # must be after we create instance of flask in line above

dictionary = {1:"Value 1", 2:"Value 2", 3:"Value 3", 4:"Value 4", 5:"Value 5"}

# View Function/Route Decorators

# default route view function
@app.route('/')
def t_test():
    return render_template('page1.html', v1='1', v2='2', dict = dictionary)

# page2 view function
@app.route('/page2')
def p2():
    return render_template('page2.html')

# page3 view function
@app.route('/page3/<mood>')
def p3(mood):
    return render_template('page3.html', mood=mood)
