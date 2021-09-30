from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
import requests, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

class Playlist(FlaskForm):
    song_title = StringField(
        'Song Title', 
        validators=[DataRequired()]
    )
    song_artist = StringField(
        'Song Artist', 
        validators=[DataRequired()]
    )

playlist = []

def store_song(my_song, my_artist):
    playlist.append(dict(
        song = my_song,
        date = datetime.today(),
        artist = my_artist
    ))

@app.route('/', methods=('GET', 'POST'))
def index():
    form = Playlist()
    if form.validate_on_submit():
        store_song(form.song_title.data, form.song_artist.data)
        return redirect('/view_playlist')
    return render_template('index.html', form=form)

@app.route('/view_playlist')
def vp():
    return render_template('vp.html', playlist=playlist)





# better to replace this with your own key from https://api.nasa.gov/
my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'

payload = {
  'api_key': my_key,
  'start_date': '2020-11-05',
  'end_date': '2020-11-08'
}

endpoint = 'https://api.nasa.gov/planetary/apod'

@app.route('/nasa')
def main():
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template('home.html', data=data)

