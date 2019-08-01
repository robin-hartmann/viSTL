# -*- coding: utf-8 -*-
from const import EXAMPLES_DIR, OUTPUT_DIR, DEFAULT_INPUT_DIR, DEFAULT_TABLE
from text2braille import text2braille
from unicode2png import unicode2png
from png2stl import png2stl


def test_img2stl():
    fname = EXAMPLES_DIR + 'hello_world.png'
    print('Processing test image: %s' % fname)
    png2stl(
        fname,
        OUTPUT_DIR,
        smoothing=1,
        scale=0.15,
    )


def test_braille2stl():
    braille = u"⠠⠓⠑⠇⠇⠕⠀⠠⠸⠺⠖"
    print("Processing braille: '%s'" % "Hello World!")
    png = DEFAULT_INPUT_DIR + "braille_to_png.png"
    unicode2png(braille, png)
    png2stl(
        png,
        OUTPUT_DIR,
        smoothing=2,
        red_factor=4,
        scale=0.009,
    )


def test_txt2braille():
    txt = EXAMPLES_DIR + 'hello_world.txt'
    braille = text2braille(txt, DEFAULT_TABLE)
    print(braille)


def run_tests():
    test_img2stl()
    test_braille2stl()
    test_txt2braille()
