PY=python3 -m py_compile
.PHONY:
    all
    test
    install
    compile
all:
    @+make test
    @make install
test:
    nosetest
install:
    python3 setup.py\
    install
compile:
    $(PY) test.py
circle:
    # of life
    circle
empty:
    # this is a comment