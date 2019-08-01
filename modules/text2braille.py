from const import TABLES_PATH, BIN_NAME, BIN_PATH_WINDOWS
from platform import system
from subprocess import check_output


def text2braille(fname, tname):
    binary = get_bin_path()
    tables = get_table_path('unicode.dis') + ',' + get_table_path(tname)
    braille = check_output([binary, tables], stdin=open(fname, 'r'))
    return braille


def is_win():
    return system() == 'Windows'


def get_bin_path():
    if is_win():
        return BIN_PATH_WINDOWS
    else:
        return BIN_NAME


def get_table_path(tname):
    if is_win():
        return TABLES_PATH + tname
    else:
        return tname
