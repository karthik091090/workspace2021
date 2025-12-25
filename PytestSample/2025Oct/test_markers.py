import pytest


### Test Execution
# pytest test_markers.py -s -v -m functional
@pytest.mark.functional
def test_first_sample():
    print("Executing first sample")
    
@pytest.mark.functional
def test_second_sample():
    print("Executing second sample")
    
@pytest.mark.regression
def test_third_sample():
    print("Executing third sample")
 
@pytest.mark.skip    ### skip a test
@pytest.mark.functional
def test_fourth_sample():
    print("Executing fourth sample")