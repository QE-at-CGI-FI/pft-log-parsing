import pytest

@pytest.fixture()
def log_content():
    #before yield is setup
    with open("data/app.log") as f:
        log = f.read()
    #yield is where you say what your tests get to use after setup
    yield log
    #after yield is teardown
    f.close()

def test_log_has_no_errors(log_content):
    assert "ERROR" not in log_content
    
def test_log_has_no_unexpected_warnings(log_content):
    assert all("low" in line for line in log_content.splitlines() if "WARNING" in line)