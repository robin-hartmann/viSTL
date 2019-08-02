# -*- coding: utf-8 -*-
from const import EXAMPLES_DIR, OUTPUT_DIR, DEFAULT_TABLE
from text2braille import text2braille
from unicode2png import unicode2png
from processor import process_inputs
from args_parser import parse_args


def run_with_args(args):
    print('Doing test run using args "%s"' % args)
    parsed_args = parse_args(args)
    process_inputs(parsed_args)


def test_img2stl():
    print('Running test img2stl')
    fname_png = EXAMPLES_DIR + 'hello_world.png'
    run_with_args([fname_png])


def base_test_txt2braille(fname_txt, fname_txt_braille, tname=DEFAULT_TABLE):
    print('Running test txt2braille with file "%s" and table "%s"' % (fname_txt, tname))
    braille = text2braille(fname_txt, tname)
    print('Result: "%s"' % braille)
    print('Saving result to "%s"' % fname_txt_braille)
    file_txt_braille = open(fname_txt_braille, "w")
    file_txt_braille.write(braille)
    return braille


def test_txt2braille():
    fname_txt = EXAMPLES_DIR + 'hello_world.txt'
    fname_txt_braille = OUTPUT_DIR + 'txt2braille.txt'
    return base_test_txt2braille(fname_txt, fname_txt_braille)


def test_txt2braille_big_en():
    fname_txt = EXAMPLES_DIR + 'dickens.txt'
    fname_txt_braille = OUTPUT_DIR + 'test_big_en.txt'
    return base_test_txt2braille(fname_txt, fname_txt_braille, 'en-GB-g2.ctb')


def test_txt2braille_big_de():
    fname_txt = EXAMPLES_DIR + 'goethe.txt'
    fname_txt_braille = OUTPUT_DIR + 'test_big_de.txt'
    return base_test_txt2braille(fname_txt, fname_txt_braille)


def base_test_braille2stl(braille, fname_png):
    print('Running test braille2stl with braille of length %d' % len(braille))
    unicode2png(braille, fname_png)
    run_with_args([fname_png])


def test_braille2stl():
    braille = u'⠠⠓⠑⠇⠇⠕⠀⠠⠸⠺⠖'  # "Hello World!"
    fname_png = OUTPUT_DIR + 'test_braille2stl.png'
    base_test_braille2stl(braille, fname_png)


def test_braille2stl_big_en(braille):
    print('Processing braille: Dickens')
    fname_png = OUTPUT_DIR + 'test_braille2stl_big_en.png'
    base_test_braille2stl(braille, fname_png)


def test_braille2stl_big_de(braille):
    print('Processing braille: Goethe')
    fname_png = OUTPUT_DIR + 'test_braille2stl_big_de.png'
    base_test_braille2stl(braille, fname_png)


def run_tests():
    test_txt2braille()
    test_braille2stl()
    test_img2stl()
    big_en_braille = test_txt2braille_big_en()
    big_de_braille = test_txt2braille_big_de()
    test_braille2stl_big_en(big_en_braille)
    test_braille2stl_big_de(big_de_braille)
