import pytest

@pytest.fixture(scope='module')
def modulesetup():
    print("module setup")
    yield
    print("module teardown")
    
@pytest.fixture(scope='function')
def functionsetup():    
    print("function setup")
    yield
    print("function teardown")


# pytest test_fixtureswithdecorators.py -s -v

def test_first_sample(modulesetup,functionsetup):
    print("Executing first sample")
    
def test_second_sample(modulesetup,functionsetup):
    print("Executing second sample")
    
### another way of calling fixtures
@pytest.mark.usefixtures("modulesetup","functionsetup")
def test_third_sample():
    print("Executing third sample")
 
@pytest.mark.usefixtures("functionsetup")   
def test_fourth_sample():
    print("Executing fourth sample")