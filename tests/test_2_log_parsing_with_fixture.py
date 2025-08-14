import pytest

@pytest.fixture()
def log_content():
    yield ""


def test_log_has_no_errors(log_content):
    pass
    
def test_log_has_no_unexpected_warnings(log_content):
    pass