EXAMPLES_DIR = 'examples/'
WORKSPACE_DIR = 'workspace/'
OUTPUT_DIR = WORKSPACE_DIR + 'out/'
DEFAULT_INPUT_DIR = WORKSPACE_DIR + 'in/'

LIBLOUIS_PATH = 'third/liblouis/'
TABLES_PATH = LIBLOUIS_PATH + 'tables/'

DEFAULT_TABLE = 'de-g2.ctb'
BIN_NAME = 'lou_translate'
BIN_PATH_WINDOWS = LIBLOUIS_PATH + BIN_NAME

# be careful:
# max_width and max_depth specify the area of the base
# and max_height specifies the height of the model
MAX_WIDTH = 200
MAX_DEPTH = 200
MAX_HEIGHT = 40
