import pytest

@pytest.fixture()
def log_content():
    yield ""

def test_log_has_less_than_25_percent_warning_values(log_content):
    pass
    
def test_log_has_at_least_1_send_every_2_minutes(log_content):
    pass
    
