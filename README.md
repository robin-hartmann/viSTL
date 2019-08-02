

# viSTL: Visual to .STL
# Table of Contents

1.  [**viSTL: Visual to .STL**](#orgb4e5bf4)
    1.  [Requirements](#org42d7638)
        1.  [All platforms](#org26ffc1d)
        2.  [Linux](#orgc8752ac)
        3.  [MacOS](#org945c82d)
        4.  [Windows](#orga446c34)
        5.  [All others platforms except Windows](#org4fbcbd7)
    2.  [Installation](#orgd59a21d)
    3.  [Running in CLI](#org4b764a9)
        1.  [Getting help](#org3f1b23c)
        2.  [Examples](#org65e8795)
        3.  [Additional options](#org3fb9a32)

## Requirements

### All platforms

-   [Python 2.7](https://www.python.org/downloads/)
-   [Pipenv](https://github.com/pypa/pipenv)

        pip install pipenv
        
### Windows

Firstly, you need to make sure, that you have [Microsoft Visual C++ 9.0](http://aka.ms/vcpython27) preinstalled. The required binary from `liblouis` is already included in this repository.

### UNIX
Make sure that `lou_translate` from `liblouis` can be executed from your shell directly, without specifying the path. Just add it to your PATH environment variable, if it isn't already included. Keep reading to find out how to get `lou_translate`.

#### Linux

There should be a `liblouis` package in all main Linux distributions. Just to list a few:

-   **Arch-based distros**:

        sudo pacman -S liblouis

-   **Debian-based distros**:

        sudo apt-get install liblouis-bin

#### macOS

Install these packages before building the `liblouis`:

    brew install automake libtool pkg-config texinfo

For further information refer to [this document](https://github.com/liblouis/liblouis/blob/master/HACKING).

## Installation

The programm uses `pipenv` as the package and virtual env manager. All the dependencies and used packages are declared in Pipfile. To prepare the environment execute the following command:

    pipenv install


<a id="org4b764a9"></a>

## Running in CLI

Firstly, you'll need to get into the program's virtual environment:

    pipenv shell


<a id="org3f1b23c"></a>

### Getting help

To get the list of possible CLI-arguments, execute the program with `-h` flag:

    python main.py -h

**Here is the list of possible arguments**:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Parameter</th>
<th scope="col" class="org-left">Description</th>
<th scope="col" class="org-left">Default</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">&#60;positional&#62;</td>
<td class="org-left">One or multiple input files separated by spaces</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">-t</td>
<td class="org-left">Name of the language table in liblouis (see `third/liblouis/tables`)</td>
<td class="org-left">`de-g2.ctb`</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">-d</td>
<td class="org-left">Input directory to search for input files if no inputs are specified</td>
<td class="org-left">`workspace/in_png_txt/`</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">-inv</td>
<td class="org-left">If set, the image will be inverted</td>
<td class="org-left">False</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">-test</td>
<td class="org-left">If set, tests will be run instead of processing inputs</td>
<td class="org-left">False</td>
</tr>
</tbody>
</table>


<a id="org65e8795"></a>

### Examples

-   **Converting all .PNGs and .TXTs to .STL**:
    -   From default directory (`workspace/in_png_txt/`):

            python main.py

    -   From specific directory:

            python main.py -d /my/example/dir

-   **Converting specific images to .STL**:

        python main.py ./examples/hello_world.png ./examples/braille.png


<a id="org3fb9a32"></a>

### Additional options

-   **Inverting images**:

        python main.py -inv

-   **Specifying the Braille language**:

        python main.py ./examples/dickens.txt -t=en-GB-g2.ctb
