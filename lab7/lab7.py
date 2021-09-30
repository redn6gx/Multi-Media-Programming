# Bobby Davis
# Lab 7

# TASK 1
    # line 514
    # class Image:

#-------------------------------------------------------------------------------------------------------------------------------

# TASK 2
    #line 515
        # """
        # This class represents an image object.  To create
        # :py:class:`~PIL.Image.Image` objects, use the appropriate factory
        # functions.  There's hardly ever any reason to call the Image constructor
        # directly.
        # * :py:func:`~PIL.Image.open`
        # * :py:func:`~PIL.Image.new`
        # * :py:func:`~PIL.Image.frombytes`
        # """

#-------------------------------------------------------------------------------------------------------------------------------

# TASK 3
print('TASK 3\n')

from PIL import Image

mountain = Image.open('mountain.jpg')
print(dir(mountain), '\n')

# getbands
# The getbands function is used to see what color bands are used in a specific image object.
# The return type is a tuple of strings
# Example: mountain image is and RGB image
#          mountain.getbands() returns ("R", "G", "B")
bands = mountain.getbands()
print(f'Color bands for mountain.jpg: {bands}\n')

#-------------------------------------------------------------------------------------------------------------------------------

# TASK 4
print('TASK 4\n')

class Song:
    """ A class to represent a song a song """
    def __init__(self, artist, genre, length, album):
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album

    def __str__(self):
        return f'\nSONG DETAILS\nArtist: {self.artist} \nGenre: {self.genre} \nLength: {self.length} sec \nAlbum: {self.album}'

Tornado_of_Souls = Song('Megadeth', 'Thrash-Metal', 319, 'Rust in Peace')
print(Tornado_of_Souls)

GOAT = Song('Polyphia', 'Progressive-Rock', 215, 'New Levels New Devils')
print(GOAT)

Acend = Song('TheDooo', 'Alternative-Metal', 190, 'Single')
print(Acend)
