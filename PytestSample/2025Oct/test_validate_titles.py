import pytest

####  pytest test_validate_titles.py -s -v 

def test_validate_title():
    print("Validating page title")
    actualtitle = "Welcome to Pytest"
    expectedtitle = "Welcome to Pytest 123"
    assert actualtitle == expectedtitle, "Title does not match!"
 
def test_validate2():
    print("Assert with in statement")
    actualtitle = "worlds"
    expectedtitle = "Welcome to Pytest world"
    assert actualtitle in expectedtitle, f"{actualtitle} not present in {expectedtitle}"
    
def test_validate3():
    print("Validating numbers")
    num1 = 10
    num2 = 20
    assert num1 > num2, "num1 is not greater than num2"

def test_validate4():
    print("Forcefully fail test")
    assert False, "Forcefully fail test"
    
    
def test_validate5():
    print("Soft Assertions Demo: Continue on failure")
    
    actualtitle = "Welcome to Pytest"
    expectedtitle = "Welcome to Pytest 123"
    assert actualtitle == expectedtitle, "Title does not match!"
 
    print("Assert with in statement")
    actualtitle = "worlds"
    expectedtitle = "Welcome to Pytest world"
    assert actualtitle in expectedtitle, f"{actualtitle} not present in {expectedtitle}"
    

    print("Validating numbers")
    num1 = 10
    num2 = 20
    assert num1 > num2, "num1 is not greater than num2"


    print("Forcefully fail test")
    assert False, "Forcefully fail test"