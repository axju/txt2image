from random import choice
from txt2image.basic import BasicImage

class QuoteImage(BasicImage):

    def __init__(self, templates, watermark=['@full.stack.hero', 'Garuda']):
        self.templates = templates
        self.watermark = watermark

    def create(self, author, quote, image, font, color):
        self._background_load(image)

        self.add_text_box_auto(quote, font=font, color=color, size=(80,60), spacing=20, pos=(50, 40))
        self.add_text(author, font=font, color=color, size=4, pos=(25,85))

        if self.watermark:
            self.add_text(self.watermark[0], font=self.watermark[1], color=color, size=3, pos=(91,98))

    def test(self, author, quote):
        for i, t in enumerate(self.templates):
            for j, font in enumerate(t['fonts']):
                for k, image in enumerate(t['images']):
                    print(f'test_{i}_{j}_{k}.png', font, image)
                    self.create(author, quote, image, font, color=t['color'])
                    self.save(f'test_{i}_{j}_{k}.png')

    def random(self, author, quote):
        template = choice(self.templates)
        image = choice(template['images'])
        font = choice(template['fonts'])
        self.create(author, quote, image, font, color=template['color'])
