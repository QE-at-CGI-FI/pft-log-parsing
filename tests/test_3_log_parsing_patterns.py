import pytest
from datetime import datetime

@pytest.fixture()
def log_content():
    with open("data/app.log") as f:
        log = f.read()
    yield log
    f.close()


@pytest.fixture
def log_entries():
    with open("data/app_full.log", encoding="utf-8") as f:
        log_text = f.read()

    entries = []
    for line in log_text.splitlines():
        try:
            ts_str, rest = line.split(" - ", 1)
            ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S,%f")
            entries.append((ts, rest))
        except ValueError:
            # Skip non-timestamp lines (tracebacks, etc.)
            continue
    return entries

@pytest.fixture
def log_lines():
    with open("data/app_full.log", encoding="utf-8") as f:
        return f.read().splitlines()

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
    
def test_timestamp_never_goes_backwards(log_entries):
    for i in range(1, len(log_entries)):
        assert log_entries[i][0] >= log_entries[i-1][0], "Timestamps went backwards"

def test_warning_low_values_treshold(log_lines):
    for line in log_lines:
        if "WARNING - Value" in line:
            value = float(line.split("Value ")[1].split(" ")[0])
            assert value < 0.20, f"WARNING flagged value {value} which is not low"

def test_error_lines_have_traceback(log_lines):
    for i, line in enumerate(log_lines):
        if "ERROR" in line:
            assert i+1 < len(log_lines), "ERROR at end of file"
            assert "Traceback" in log_lines[i+1], "ERROR not followed by traceback"

#this is script
print("This is a script, not a test")

#this is a script that tests
assert 10 > 1

#this is function, not a test
def not_a_test_function():
    print("This is a function, not a test")

#this is a test
def test_this_is_a_test():
    assert 1 == 1