import pytest
import logging
from job_matcher.context_managers import measure_block


def test_measure_block_logs_execution(caplog):
    with caplog.at_level(logging.DEBUG):
        with measure_block("Job matching"):
            result = 10 + 20

    assert result == 30
    assert "Job matching executed in" in caplog.text


def test_measure_block_logs_on_exception(caplog):    

    with caplog.at_level(logging.DEBUG):
        with pytest.raises(ZeroDivisionError):
            with measure_block("Failed operation"):
                10 / 0    

    assert "Failed operation executed in" in caplog.text

def test_measure_block_preserves_exception():
    with pytest.raises(ValueError, match="Invalid job"):
        with measure_block("Job validation"):
            raise ValueError("Invalid job")