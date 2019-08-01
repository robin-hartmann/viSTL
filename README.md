
# Table of Contents

1.  [**viSTL: Visual to .STL**](#orgbca6e24)
    1.  [Requirements](#org276a30f)
        1.  [All platforms](#org51d9b18)
        2.  [Linux](#org01675ba)
        3.  [MacOS](#orgcdbffbd)
        4.  [Windows](#org38d81df)
        5.  [All others platforms except Windows](#org9fdc9a6)
    2.  [Installation](#org1483548)
    3.  [Running in CLI](#orgc5aac58)
        1.  [Getting help](#org0f4f52b)
        2.  [Examples](#org40552d5)
        3.  [Additional options](#org162737b)


<a id="orgbca6e24"></a>

# **viSTL: Visual to .STL**


<a id="org276a30f"></a>

## Requirements


<a id="org51d9b18"></a>

### All platforms

-   [Python 2.7](https://www.python.org/downloads/)
-   [Pipenv](https://github.com/pypa/pipenv)

        pip install pipenv


<a id="org01675ba"></a>

### Linux

There should be a `liblouis` package in all main Linux distributions. Just to list a few:

-   **Arch-based distros**:

        sudo pacman -S liblouis

-   **Debian-based distros**:

        sudo apt-get install liblouis-bin


<a id="orgcdbffbd"></a>

### MacOS

Install these packages before building the `liblouis`:

    brew install automake libtool pkg-config texinfo


<a id="org38d81df"></a>

### Windows

Firstly, you need to make sure, that you have [Microsoft Visual C++ 9.0](http://aka.ms/vcpython27) preinstalled. The `liblouis` package comes preinstalled as third-party library.


<a id="org9fdc9a6"></a>

### All others platforms except Windows

   Make sure that `lou_translate` can be executed from your shell directly, without specifying the path. Or just add it to your PATH environment variable.
For further information refer to [this document](https://github.com/liblouis/liblouis/blob/master/HACKING).


<a id="org1483548"></a>

## Installation

The programm uses `pipenv` as the package and virtual env manager. All the dependencies and used packages are declared in Pipfile. To prepare the environment execute the following command:

    pipenv install


<a id="orgc5aac58"></a>

## Running in CLI

Firstly, you'll need to get into the program's virtual environment:

    pipenv shell


<a id="org0f4f52b"></a>

### Getting help

To get the list of possible CLI-arguments, execute the program with `-h` flag:

    python main.py -h


<a id="org40552d5"></a>

### Examples

-   **Converting all .PNGs and .TXTs to .STL**:
    -   From default directory (`.workspace/in_png_txt/`):

            python main.py

    -   From specific directory:

            python main.py -d /my/example/dir

-   **Converting specific images to .STL**:

        python main.py ./examples/hello_world.png ./examples/braille.png


<a id="org162737b"></a>

### Additional options

-   **Inverting images**:

        python main.py -inv

-   **Specifying the Braille language**:

        python main.py ./examples/dickens.txt -t=en-GB-g2.ctb
