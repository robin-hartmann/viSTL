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

    im_length, im_width = adjustImageSize(text, font)
    max_chars, num_lines = get_text_len_width_info(text)
    pix_length = im_length / len(text) * max_chars
    pix_width = im_width * num_lines

    img = Image.new(MODE_CREATION_PNG,
                    (pix_length, pix_width),
                    color=back_color)
    d = ImageDraw.Draw(img, mode=MODE_CREATION_PNG)
    d.text((0, 0), text, fill=text_color, font=font)
    img.save(fname)
    return max_chars, num_lines


def get_text_len_width_info(text):
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

    return max_chars, num_lines


def adjustImageSize(text, font):
    text_size = font.getsize(text)
    length = text_size[0]
    width = text_size[1]
    #length += -15
    #width += 5
    return length, width
