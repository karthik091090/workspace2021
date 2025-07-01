import pytest

### run at the beginning of module
def setup_module(module):
    print("module setup")

### run at the end of module
def teardown_module(module):
    print("module teardown")

### run at the beginning of each testcase
def setup_function(function):
    print("function setup")
 
### run at the end of each testcase   
def teardown_function(function):
    print("function tear down")

def test_first_sample():
    print("Executing first sample")
    
def test_second_sample():
    print("Executing second sample")