# This is an empty project for python [![Build Status](https://travis-ci.org/ADU-21/python-stencil.svg?branch=master)](https://travis-ci.org/ADU-21/python-stencil) 

```
git clone https://github.com/ADU-21/python-stencil.git
```

## Install dependences
```
pip install -r ./requirements.txt
```

## Test
```
nosetests
```

## Build
```
pyinstaller -F src/run.py --clean
```

## Run
```
./dist/run
```