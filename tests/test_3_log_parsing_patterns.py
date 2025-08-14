import pytest
from datetime import datetime

@pytest.fixture()
def log_content():
    with open("data/app.log") as f:
        log = f.read()
    yield log
    f.close()

def test_log_has_less_than_25_percent_warning_values(log_content):
    warning_lines = [line for line in log_content.splitlines() if "WARNING" in line]
    assert len(warning_lines) < 0.25 * len(log_content.splitlines())

def test_log_has_at_least_1_send_every_2_minutes(log_content):
    timestamps = []
    for line in log_content.splitlines():
            if "Sending data to server:" in line:
                ts_str = line.split(" - ")[0]
                ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S,%f")
                timestamps.append(ts)
  
    for i in range(1, len(timestamps)):
        diff = (timestamps[i] - timestamps[i - 1]).total_seconds()
        assert diff <= 120, f"Gap too large: {diff:.1f} seconds between {timestamps[i-1]} and {timestamps[i]}"
