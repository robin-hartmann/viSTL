
# Table of Contents

1.  [**viSTL: Visual to .STL**](#org88a8f6e)
    1.  [Requirements](#org940d3b0)
        1.  [All platforms](#orgffd2873)
        2.  [Linux](#orgf33f6ef)
        3.  [MacOS](#org1412caa)
        4.  [Windows](#org92153eb)
        5.  [All others platforms except Windows](#org01a12d6)
    2.  [Installation](#orgdeb24e1)
    3.  [Running in CLI](#org87f79de)
        1.  [Getting help](#orgd1d40bb)
        2.  [Examples](#org6e29105)
        3.  [Additional options](#orgf62931e)


<a id="org88a8f6e"></a>

# **viSTL: Visual to .STL**


<a id="org940d3b0"></a>

## Requirements


<a id="orgffd2873"></a>

### All platforms

-   [Python 2.7](https://www.python.org/downloads/)
-   [Pipenv](https://github.com/pypa/pipenv)

        pip install pipenv


<a id="orgf33f6ef"></a>

### Linux

There should be a `liblouis` package in all main Linux distributions. Just to list a few:

-   **Arch-based distros**:

        sudo pacman -S liblouis

-   **Debian-based distros**:

        sudo apt-get install liblouis-bin


<a id="org1412caa"></a>

### MacOS

Install these packages before building the `liblouis`:

    brew install automake libtool pkg-config texinfo


<a id="org92153eb"></a>

### Windows

Firstly, you need to make sure, that you have [Microsoft Visual C++ 9.0](http://aka.ms/vcpython27) preinstalled. The `liblouis` package comes preinstalled as third-party library.


<a id="org01a12d6"></a>

### All others platforms except Windows

   Make sure that `lou_translate` can be executed from your shell directly, without specifying the path. Or just add it to your PATH environment variable.
For further information refer to [this document](https://github.com/liblouis/liblouis/blob/master/HACKING).


<a id="orgdeb24e1"></a>

## Installation

The programm uses `pipenv` as the package and virtual env manager. All the dependencies and used packages are declared in Pipfile. To prepare the environment execute the following command:

    pipenv install


<a id="org87f79de"></a>

## Running in CLI

Firstly, you'll need to get into the program's virtual environment:

    pipenv shell


<a id="orgd1d40bb"></a>

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
<td class="org-left">-t</td>
<td class="org-left">Name of the language table in liblouis</td>
<td class="org-left">de-g2.ctb</td>
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
<td class="org-left">-d</td>
<td class="org-left">Output directory with .STL-Data</td>
<td class="org-left">`workspace/out_stl`</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left"><inputs></td>
<td class="org-left">Positional parameter. The filenames are expected separated by space</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="org6e29105"></a>

### Examples

-   **Converting all .PNGs and .TXTs to .STL**:
    -   From default directory (`workspace/in_png_txt/`):

            python main.py

    -   From specific directory:

            python main.py -d /my/example/dir

-   **Converting specific images to .STL**:

        python main.py ./examples/hello_world.png ./examples/braille.png


<a id="orgf62931e"></a>

### Additional options

-   **Inverting images**:

        python main.py -inv

-   **Specifying the Braille language**:

        python main.py ./examples/dickens.txt -t=en-GB-g2.ctb
