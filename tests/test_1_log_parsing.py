
def test_log_has_no_errors():
    with open("data/app.log") as f:
        log_contents = f.read()
        assert "ERROR" not in log_contents

def test_log_has_no_unexpected_warnings():
    with open("data/app.log") as f:
        log = f.read()
        for line in log.splitlines():
            if "WARNING" in line:
                assert "low" in line