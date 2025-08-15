from asyncio import log
import pytest

@pytest.fixture()
def log_content():
    #setup
    with open("data/app.log") as f:
        log_content = f.read()
    yield log_content
    #teardown
    f.close()


def test_log_has_no_errors(log_content):
    assert "ERROR" not in log_content

    
def test_log_has_no_unexpected_warnings(log_content):
    for line in log_content.splitlines():
        if "WARNING" in line:
            assert "low" in line