
# Table of Contents

1.  [**viSTL: Visual to .STL**](#org8d22e61)
    1.  [Requirements](#orge6d9fb3)
        1.  [All platforms](#org855f172)
        2.  [Linux](#org73d664f)
        3.  [MacOS](#orgb8eba81)
        4.  [Windows](#org65df5b4)
        5.  [All others platforms except Windows](#org5fe3bda)
    2.  [Installation](#org5fefaf0)
    3.  [Running in CLI](#org1214c63)
        1.  [Getting help](#org2899444)
        2.  [Examples](#orgcafad96)
        3.  [Additional options](#orgdd393fc)


<a id="org8d22e61"></a>

# **viSTL: Visual to .STL**


<a id="orge6d9fb3"></a>

## Requirements


<a id="org855f172"></a>

### All platforms

-   [Python 2.7](https://www.python.org/downloads/)
-   [Pipenv](https://github.com/pypa/pipenv)

        pip install pipenv


<a id="org73d664f"></a>

### Linux

There should be a `liblouis` package in all main Linux distributions. Just to list a few:

-   **Arch-based distros**:

        sudo pacman -S liblouis

-   **Debian-based distros**:

        sudo apt-get install liblouis-bin


<a id="orgb8eba81"></a>

### MacOS

Install these packages before building the `liblouis`:

    brew install automake libtool pkg-config texinfo


<a id="org65df5b4"></a>

### Windows

Firstly, you need to make sure, that you have [Microsoft Visual C++ 9.0](http://aka.ms/vcpython27) preinstalled. The `liblouis` package comes preinstalled as third-party library.


<a id="org5fe3bda"></a>

### All others platforms except Windows

   Make sure that `lou_translate` can be executed from your shell directly, without specifying the path. Or just add it to your PATH environment variable.
For further information refer to [this document](https://github.com/liblouis/liblouis/blob/master/HACKING).


<a id="org5fefaf0"></a>

## Installation

The programm uses `pipenv` as the package and virtual env manager. All the dependencies and used packages are declared in Pipfile. To prepare the environment execute the following command:

    pipenv install


<a id="org1214c63"></a>

## Running in CLI

Firstly, you'll need to get into the program's virtual environment:

    pipenv shell


<a id="org2899444"></a>

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
<th scope="col" class="org-left">**Parameter**</th>
<th scope="col" class="org-left">**Description**</th>
<th scope="col" class="org-left">**Default**</th>
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
<td class="org-left">workspace/out<sub>stl</sub></td>
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


<a id="orgcafad96"></a>

### Examples

-   **Converting all .PNGs and .TXTs to .STL**:
    -   From default directory (`workspace/in_png_txt/`):

            python main.py

    -   From specific directory:

            python main.py -d /my/example/dir

-   **Converting specific images to .STL**:

        python main.py ./examples/hello_world.png ./examples/braille.png


<a id="orgdd393fc"></a>

### Additional options

-   **Inverting images**:

        python main.py -inv

-   **Specifying the Braille language**:

        python main.py ./examples/dickens.txt -t=en-GB-g2.ctb
