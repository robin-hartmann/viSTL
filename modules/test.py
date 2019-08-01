# -*- coding: utf-8 -*-
from const import EXAMPLES_DIR, OUTPUT_DIR, DEFAULT_INPUT_DIR, DEFAULT_TABLE
from util import get_new_fname
from text2braille import text2braille
from unicode2png import unicode2png
from png2stl import png2stl


def test_img2stl():
    fname_png = EXAMPLES_DIR + 'hello_world.png'
    print('Processing test image: "%s"' % fname_png)
    fname_stl = get_new_fname(fname_png, OUTPUT_DIR, 'stl')
    png2stl(
        fname_png,
        fname_stl,
        smoothing=1,
        scale=0.15,
    )


def test_braille2stl():
    braille = u"⠠⠓⠑⠇⠇⠕⠀⠠⠸⠺⠖"
    print('Processing braille: "%s"' % 'Hello World!')
    fname_png = DEFAULT_INPUT_DIR + 'test_braille2stl.png'
    unicode2png(braille, fname_png)
    fname_stl = get_new_fname(fname_png, OUTPUT_DIR, 'stl')
    png2stl(
        fname_png,
        fname_stl,
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
