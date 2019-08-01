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
        scale=0.15)


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
        scale=0.012,
        min_thickness_percent=0.2)


def test_txt2braille():
    txt = EXAMPLES_DIR + 'hello_world.txt'
    braille = text2braille(txt, DEFAULT_TABLE)
    print(braille)


def test_txt2braille_big_en():
    txt = EXAMPLES_DIR + 'dickens.txt'
    braille = text2braille(txt, 'en-GB-g2.ctb')
    print('Dickens:\n"%s"' % braille)
    return braille


def test_txt2braille_big_de():
    txt = EXAMPLES_DIR + 'goethe.txt'
    braille = text2braille(txt, DEFAULT_TABLE)
    print('Goethe:\n"%s"' % braille)
    return braille


def test_braille2stl_big_en(braille):
    print('Processing braille: "%s"' % 'Dickens')
    fname_png = DEFAULT_INPUT_DIR + 'test_braille2stl_big_en.png'
    unicode2png(braille, fname_png)
    fname_stl = get_new_fname(fname_png, OUTPUT_DIR, 'stl')
    png2stl(
        fname_png,
        fname_stl,
        smoothing=2,
        red_factor=4,
        scale=0.012,
        min_thickness_percent=0.2)


def test_braille2stl_big_de(braille):
    print('Processing braille: "%s"' % 'Goethe')
    fname_png = DEFAULT_INPUT_DIR + 'test_braille2stl_big_de.png'
    unicode2png(braille, fname_png)
    fname_stl = get_new_fname(fname_png, OUTPUT_DIR, 'stl')
    png2stl(
        fname_png,
        fname_stl,
        smoothing=2,
        red_factor=4,
        scale=0.012,
        min_thickness_percent=0.2)


def run_tests():
    test_img2stl()
    test_braille2stl()
    test_txt2braille()
    test_braille2stl_big_en(test_txt2braille_big_en())
    test_braille2stl_big_de(test_txt2braille_big_de())
