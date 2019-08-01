from PIL import Image, ImageDraw, ImageFont
from util import is_win

MODE_CREATION_PNG = 'RGBA'
PATH_FONT_WIN = 'third/fonts/UBraille.ttf'
PATH_FONT_UNIX = 'third/fonts/applebraille.ttf'


def unicode2png(text, fname):
    back_color = (0, 0, 0, 255)
    text_color = (255, 255, 255)
    font_type = PATH_FONT_WIN if is_win() else PATH_FONT_UNIX
    font = ImageFont.truetype(font_type, 100)
    length, width = adjustImageSize(text, font)

    # Line/character counting
    num_lines = 1
    max_chars = 0
    num_chars = 0
    for c in text:
        if c == '\n':
            num_lines += 1
            if num_chars > max_chars:
                max_chars = num_chars

            num_chars = 0
        else:
            num_chars += 1

    if num_lines == 1:
        max_chars = len(text)

    img = Image.new(MODE_CREATION_PNG,
                    ((length / len(text)) * max_chars, width * num_lines),
                    color=back_color)
    d = ImageDraw.Draw(img, mode=MODE_CREATION_PNG)
    d.text((0, 0), text, fill=text_color, font=font)
    img.save(fname)


def adjustImageSize(text, font):
    text_size = font.getsize(text)
    length = text_size[0]
    width = text_size[1]
    #length += -15
    #width += 5
    return length, width
