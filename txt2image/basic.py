from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap

from txt2image.misc import random_color

class BasicImage:

    def __init__(self, **kwagrs):

        size = kwagrs.get('size', (1024, 1024))
        self._background_color(size)

        if 'color' in kwagrs:
            self._background_color(size, rgb=kwagrs['color'])

        if 'image' in kwagrs:
            self._background_load(kwagrs['image'])

    def _background_color(self, size, rgb=random_color()):
        self.img = Image.new("RGB", size, rgb)
        self.draw = ImageDraw.Draw(self.img)

    def _background_load(self, filename):
        self.img = Image.open(filename)
        self.draw = ImageDraw.Draw(self.img)

    @property
    def size(self):
        return self.img.size

    def get_pos(self, w, h, pos):
        return (int((self.size[0]*pos[0]/100)-0.5*w), int((self.size[1]*pos[1]/100)-0.5*h))

    def get_font(self, filename, size=70, text='Üq'):
        """
        Load the font dependen on the image size.
        7 >> 7 % of the image size
        """
        fontsize = 1
        while True:
            font = ImageFont.truetype(filename, fontsize)
            if font.getsize(text)[1] > self.size[0]*size/100:
                return ImageFont.truetype(filename, fontsize-1)

            fontsize += 1

    def get_text(self, text, font, width):
        """
        Get the text in the right width
        """
        _width = 1
        while True:
            para = wrap(text, width=_width)
            if self.draw.textsize('\n'.join(para), font=font)[0] > self.size[0]*width/100:
                para = wrap(text, width=_width-1)
                return '\n'.join(para)

            _width += 1

    def _ist(self, x, text, font, spacing):
        _font = ImageFont.truetype(font, int(x[1]))
        para = wrap(text, width=int(x[0]))
        return self.draw.textsize('\n'.join(para), font=_font, spacing=spacing)

    def find_box(self, text, font, size, spacing):
        soll = self.size[0]*size[0]/100, self.size[1]*size[1]/100
        x = [len(text),1]
        work = True
        while work:
            work = 0
            ist = self._ist(x, text, font, spacing)
            while ist[0]<=soll[0] and ist[1]<soll[1]:
                x[1] += 1
                ist = self._ist(x, text, font, spacing)
                work = 2

            while ist[0]>soll[0] and x[0]>20:
                x[0] -= 1
                ist = self._ist(x, text, font, spacing)
                work = 1

        return ImageFont.truetype(font, int(x[1])), '\n'.join(wrap(text, width=int(x[0])))


    def add_text(self, text, font='Garuda', color=(255,255,255), size=10, pos=(50, 50)):
        _font = self.get_font(font, size, text)
        w, h = self.draw.textsize(text, font=_font)
        self.draw.text(self.get_pos(w, h, pos), text, font=_font, fill=color)

    def add_text_box(self, text, width, font='Garuda', spacing=10, color=(255,255,255), size=10, pos=(50, 50)):
        _font = self.get_font(font, size, text)
        _text = self.get_text(text, _font, width)
        w, h = self.draw.textsize(_text, font=_font, spacing=spacing)
        P = self.get_pos(w, h, pos)
        self.draw.multiline_text(P, _text, font=_font, fill=color, align='center', spacing=spacing)

    def add_text_box_auto(self, text, font='Garuda', spacing=10, color=(255,255,255), size=(90, 90), pos=(50, 50)):
        _font, _text = self.find_box(text, font, size, spacing)
        w, h = self.draw.textsize(_text, font=_font, spacing=spacing)
        P = self.get_pos(w, h, pos)
        self.draw.multiline_text(P, _text, font=_font, fill=color, align='center', spacing=spacing)

    def save(self, filename):
        self.img.save(filename)
