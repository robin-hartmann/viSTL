
# Table of Contents

1.  [**viSTL: Visual to .STL**](#orgd638306)
    1.  [Requirements](#org787e40b)
        1.  [All platforms](#org3aa7344)
        2.  [Linux](#org860b0a2)
        3.  [MacOS](#org6d5d21e)
        4.  [Windows](#org5475e49)
        5.  [All others platforms except Windows](#org209427c)
    2.  [Installation](#orge995813)
    3.  [Running in CLI](#org5e9e586)
        1.  [Getting help](#org82f667d)
        2.  [Examples](#orgbbe410d)
        3.  [Additional options](#org0527397)


<a id="orgd638306"></a>

# **viSTL: Visual to .STL**


<a id="org787e40b"></a>

## Requirements


<a id="org3aa7344"></a>

### All platforms

-   [Python 2.7](https://www.python.org/downloads/)
-   [Pipenv](https://github.com/pypa/pipenv)

        pip install pipenv


<a id="org860b0a2"></a>

### Linux

There should be a `liblouis` package in all main Linux distributions. Just to list a few:

-   **Arch-based distros**:

        sudo pacman -S liblouis

-   **Debian-based distros**:

        sudo apt-get install liblouis-bin


<a id="org6d5d21e"></a>

### MacOS

Install these packages before building the `liblouis`:

    brew install automake libtool pkg-config texinfo


<a id="org5475e49"></a>

### Windows

Firstly, you need to make sure, that you have [Microsoft Visual C++ 9.0](http://aka.ms/vcpython27) preinstalled. The `liblouis` package comes preinstalled as third-party library.


<a id="org209427c"></a>

### All others platforms except Windows

   Make sure that `lou_translate` can be executed from your shell directly, without specifying the path. Or just add it to your PATH environment variable.
For further information refer to [this document](https://github.com/liblouis/liblouis/blob/master/HACKING).


<a id="orge995813"></a>

## Installation

The programm uses `pipenv` as the package and virtual env manager. All the dependencies and used packages are declared in Pipfile. To prepare the environment execute the following command:

    pipenv install


<a id="org5e9e586"></a>

## Running in CLI

Firstly, you'll need to get into the program's virtual environment:

    pipenv shell


<a id="org82f667d"></a>

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
<th scope="col" class="org-left">Bedeutung</th>
<th scope="col" class="org-left">Default</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">-t</td>
<td class="org-left">Name der Sprachtabelle in liblouis</td>
<td class="org-left">de-g2.ctb</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">-inv</td>
<td class="org-left">Wenn eingegeben, wird das Bild invertiert</td>
<td class="org-left">False</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">-d</td>
<td class="org-left">Ausgabeverzeichniss mit `.STL`-Dateien</td>
<td class="org-left">`workspace/out_stl`</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left"><inputs></td>
<td class="org-left">Positionalles Parameter. Es werden</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">die Dateiennamen leerzeichengetrennt</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">erwartet</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="orgbbe410d"></a>

### Examples

-   **Converting all .PNGs and .TXTs to .STL**:
    -   From default directory (`workspace/in_png_txt/`):

            python main.py

    -   From specific directory:

            python main.py -d /my/example/dir

-   **Converting specific images to .STL**:

        python main.py ./examples/hello_world.png ./examples/braille.png


<a id="org0527397"></a>

### Additional options

-   **Inverting images**:

        python main.py -inv

-   **Specifying the Braille language**:

        python main.py ./examples/dickens.txt -t=en-GB-g2.ctb
