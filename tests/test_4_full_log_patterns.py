import pytest
from datetime import datetime

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


def test_no_large_time_gaps(log_entries):
    for i in range(1, len(log_entries)):
        delta = (log_entries[i][0] - log_entries[i-1][0]).total_seconds()
        assert delta <= 120, f"Gap too large between {log_entries[i-1]} and {log_entries[i]}"


def test_timestamp_never_goes_backwards(log_entries):
    for i in range(1, len(log_entries)):
        assert log_entries[i][0] >= log_entries[i-1][0], "Timestamps went backwards"


def test_info_followed_by_data_match(log_lines):
    last_data_by_source = {}
    for line in log_lines:
        if "DEBUG - Data:" in line:
            parts = line.split(" - ")
            source = parts[1]
            value = parts[-1].split(": ")[1]
            last_data_by_source[source] = value
        if "INFO - Sending data" in line:
            parts = line.split(" - ")
            source = parts[1]
            sent_value = parts[-1].split(": ")[1]
            assert source in last_data_by_source, f"No previous data for {source}"
            assert sent_value == last_data_by_source[source], (
                f"Mismatch for {source}: sent {sent_value}, expected {last_data_by_source[source]}"
            )


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
