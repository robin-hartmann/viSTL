

# **viSTL: Visual to .STL**


## Requirements


### All platforms

-   [Python 2.7](https://www.python.org/downloads/)
-   [Pipenv](https://github.com/pypa/pipenv)

        pip install pipenv


### Linux

There is already a package in all main Linux distributions repositories.

-   **Arch-based distros**:

        sudo pacman -S liblouis
-   **Debian-based distros**:

        sudo apt-get install liblouis-bin


### MacOS

Install these packages before building the `liblouis`

    brew install automake libtool pkg-config texinfo


### Windows

Firstly, you need to make sure, that you have [Microsoft Visual C++ 9.0](http://aka.ms/vcpython27) preinstalled. The `liblouis` package comes preinstalled as third-party library.


### All others platforms except Windows

   Make sure that `lou_translate` can be executed from your shell directly, without specifying the path. Or just add it to your PATH environment variable.
For further information refer to [this document](https://github.com/liblouis/liblouis/blob/master/HACKING).


## Installation

The programm uses `pipenv` as the package and virtual env manager. All the dependencies and used packages are declared in Pipfile. To prepare the environment execute the following command:

    pipenv install


## Running in CLI

Firstly, you'll need to get into the program's virtual environment:

    pipenv shell


### Getting help

To get the list of possible CLI-arguments, execute the program with `-h` flag:

    python main.py -h


### Examples

-   **Converting all .PNGs and .TXTs to .STL**:
    -   From default directory (`.workspace/in_png_txt/`):

            python main.py
    -   From specific directory:

            python main.py -d /my/example/dir
-   **Converting specific images to .STL**:

        python main.py ./examples/hello_world.png ./examples/braille.png


### Additional options

-   **Inverting images**:

        python main.py -inv
-   **Specifying the Braille language**:

        python main.py ./examples/dickens.txt -t=en-GB-g2.ctb
