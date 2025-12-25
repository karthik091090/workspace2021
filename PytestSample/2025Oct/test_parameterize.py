import pytest


@pytest.mark.parametrize("username,password", [
    ('admin1', 'adminpass1'),   
    ('admin2', 'adminpass2'),
    ('admin3', 'adminpass3')
])
def test_dologin(username, password):
    print("Executing login test")
    print(f"Username: {username}, Password: {password}")