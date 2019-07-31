# viSTL

## Requirements

### All platforms

- [Python 2.7](https://www.python.org/downloads/)
- [Pipenv](https://github.com/pypa/pipenv)
    - `pip install pipenv`

### Only Windows

- [Microsoft Visual C++ 9.0](http://aka.ms/vcpython27)

### All platforms except Windows

- `lou_translate` in PATH (from [liblouis](https://github.com/liblouis/liblouis))
    - use package manager of os to install
        - Arch Linux: `sudo pacman -S liblouis`

## Installation

```bash
pipenv install
```

## Running

```bash
pipenv shell
python main.py -h
```