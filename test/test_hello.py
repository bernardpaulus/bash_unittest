#!/bin/env python

import subprocess
import unittest
import os.path

class BashFunctionCaller(object):
    def __init__(self, script):
        self.script = script
        
    def __getattr__(self, name):
        def call_fun(*args):
            script_path = fn = "'{}'".format(os.path.join(os.path.dirname(__file__), self.script))
            return subprocess.check_output(
                    ['bash', '-c', 'source {} && {} {}'.format(script_path, name, " ".join(args))],
                    universal_newlines=True)
            
        return call_fun
        
class HelloTest(unittest.TestCase):
    def setUp(self):
        self.script = BashFunctionCaller("../src/hello.sh")
        
    def test_hello_world(self):
        output = self.script.hello("world")
        self.assertEqual("hello world\n", output)