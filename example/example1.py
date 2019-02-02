from txt2image.basic import BasicImage
from txt2image.misc import random_color

text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'

# created different sizes
for i in range(4,11):
    size=(2**i, 2**i)
    img = BasicImage(size=size)
    img.add_text('Hello World', size=10)
    img.add_text('@full.stack.hero', size=3, pos=(91,98))
    img.save(f'test_size_{size[0]}.png')

# created different colors
for i in range(10):
    img = BasicImage(color=random_color())
    img.add_text('Hello World', size=10, color=random_color())
    img.add_text('@full.stack.hero', size=3, pos=(91,98))
    img.save(f'test_color_{i}.png')

# users different fonts
for font in ['Uroob', 'Karumbi', 'Purisa-Bold']:
    img = BasicImage()
    img.add_text('Hello World', font=font, size=10)
    img.add_text('@full.stack.hero', size=3, pos=(91,98))
    img.save(f'test_font_{font}.png')

# playing with box width
for i in range(2,11):
    img = BasicImage()
    img.add_text_box(text, width=i*10, size=5)
    img.add_text('@full.stack.hero', size=3, pos=(91,98))
    img.save(f'test_box_{i}.png')

# playing with box width
for i in range(4,11):
    img = BasicImage()
    img.add_text_box_auto(text, size=(i*10,i*10-5))
    img.add_text('@full.stack.hero', size=3, pos=(91,98))
    img.save(f'test_box_auto{i}.png')
