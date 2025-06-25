import pytest

def get_data():
    return  [
        ('user1','pass1'),
        ('user2','pass2'),
        ('user3','pass3'),
    ]


### Test Execution
# pytest test_parameterize.py -s -v

@pytest.mark.parametrize("username,password",get_data())
def test_one(username, password):
    print(username,"...",password)
    