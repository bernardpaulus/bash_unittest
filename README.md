Bash unit testing from python
=============================

Minimal working example of how to do bash unit testing with python's unittest

The principle, calling the bash script from python and using unittest to do the unit testing can be applied to other language/unit testing framework pairs.

Run the script
--------------

    src/hello.sh
    
Run the example unit test
-------------------------

    python -m unittest discover -s test

this outputs:

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.159s
    
    OK

Requirements
------------

bash, python 3
