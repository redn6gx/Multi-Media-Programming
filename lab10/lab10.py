from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# creat an insatance of Flask
app = Flask(__name__)
bootstrap = Bootstrap(app) # must be after we create instance of flask in line above

# View Function
# route decorator binds a function to a URL
@app.route('/')
def hello():
    return '<p>Here is an interesting fact about...(didn\'t do breakout rooms, so no facts about people)</p>'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2

@app.route('/bobby')
def t_test():
    return render_template('template.html')
