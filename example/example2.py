from txt2image.basic import BasicImage
from txt2image.misc import random_color
import requests
from random import randint

# more apis:
# https://github.com/toddmotto/public-apis#animals

def save(text, name):
    img = BasicImage(color=random_color())
    img.add_text_box_auto(text, size=(80,40), spacing=20)
    img.add_text('@full.stack.hero', size=3, pos=(91,98))
    img.save(name)
    print('save', name)


r = requests.get('https://geek-jokes.sameerkumar.website/api')
if r.status_code == 200:
    joke = r.text[1:-2]
    save(joke, 'geek_jokes_{}.png'.format(randint(10000,99999)))

r = requests.get('https://cat-fact.herokuapp.com/facts/random')
if r.status_code == 200:
    fact = r.json()['text']
    save(fact, 'cat_fact_{}.png'.format(randint(10000,99999)))

r = requests.get('https://corporatebs-generator.sameerkumar.website/')
if r.status_code == 200:
    fact = r.json()['phrase']
    save(fact, 'corporatebs_generator_{}.png'.format(randint(10000,99999)))

r = requests.get('https://api.chucknorris.io/jokes/random')
if r.status_code == 200:
    fact = r.json()['value']
    save(fact, 'chucknorris_{}.png'.format(randint(10000,99999)))

headers = {'Accept': 'application/json'}
r = requests.get('https://icanhazdadjoke.com/', headers=headers)
if r.status_code == 200:
    joke = r.json()['joke']
    save(joke, 'dadjoke{}.png'.format(randint(10000,99999)))

r = requests.get('http://api.icndb.com/jokes/random/')
if r.status_code == 200:
    joke = r.json()['value']['joke']
    save(joke, 'chucknorris_{}.png'.format(randint(10000,99999)))
