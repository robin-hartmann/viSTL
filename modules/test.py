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
    print('Processing braille2stl: Hello World!')
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
    print('Processing txt2braille: Hello World!')
    txt = EXAMPLES_DIR + 'hello_world.txt'
    braille = text2braille(txt, DEFAULT_TABLE)
    file = open(OUTPUT_DIR + "txt2braille.txt", "w")
    file.write(braille)
    print(braille)


def test_txt2braille_big_en():
    print('Processing txt2braille: Dickens')
    txt = EXAMPLES_DIR + 'dickens.txt'
    braille = text2braille(txt, 'en-GB-g2.ctb')
    file = open(OUTPUT_DIR + "test_big_en.txt", "w")
    file.write(braille)
    return braille


def test_txt2braille_big_de():
    print('Processing txt2braille: Goethe')
    txt = EXAMPLES_DIR + 'goethe.txt'
    braille = text2braille(txt, DEFAULT_TABLE)
    file = open(OUTPUT_DIR + "test_big_de.txt", "w")
    file.write(braille)
    return braille


def test_braille2stl_big_en(braille):
    print('Processing braille: Dickens')
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
    print('Processing braille: Goethe')
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
    test_txt2braille()
    test_braille2stl()
    test_img2stl()
    big_en_braille = test_txt2braille_big_en()
    big_de_braille = test_txt2braille_big_de()
    test_braille2stl_big_en(big_en_braille)
    test_braille2stl_big_de(big_de_braille)
