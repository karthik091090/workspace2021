import pytest

### fixture to pass on all test case
@pytest.mark.usefixtures("log_on_failure","page")
class BaseTest:
    pass