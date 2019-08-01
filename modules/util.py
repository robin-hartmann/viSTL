from os import path
from platform import system


def change_ext(fname, new_ext):
    return path.splitext(path.basename(fname))[0] + '.' + new_ext


def get_new_fname(fname, directory, new_ext):
    return directory + change_ext(path.basename(fname), new_ext)


def is_win():
    return system() == 'Windows'
