from txt2image.quote import QuoteImage
from random import choice, randint

fonts = ['Uroob', 'Karumbi', 'Purisa-Bold']
templates = [
    {
        'color': (255,255,255),
        'fonts': fonts,
        'images': ['backgrounds/dark.png']
    },
    {
        'color': (0,0,0),
        'fonts': fonts,
        'images': [f'backgrounds/{s}.png' for s in ['bright', 'colors']]
    },

]

img = QuoteImage(templates=templates)

author = 'Joan Miro'
quote = 'The works must be conceived with fire in the soul, but executed with clinical coolness.'
img.test(author, quote)
