from PIL import Image, ImageDraw, ImageFont

MODE_CREATION_PNG = "RGBA"
PATH_FONT = "third/fonts/applebraille.ttf"


def unicode2png(text, fname):
    back_color = (0, 0, 0, 255)
    text_color = (255, 255, 255)
    # @todo: Fix size by image creation
    img = Image.new(MODE_CREATION_PNG, (800, 100), color=back_color)
    font = ImageFont.truetype(PATH_FONT, 100)
    d = ImageDraw.Draw(img, mode=MODE_CREATION_PNG)
    d.text((10, 10), text, fill=text_color, font=font)
    img.save(fname)
