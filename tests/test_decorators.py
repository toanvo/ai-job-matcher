import logging
import pytest

from job_matcher.decorators import measure_execution_time


def test_decorator_logs_execution(caplog):
    @measure_execution_time
    def calculate_total():
        return 100

    with caplog.at_level(logging.DEBUG):
        result = calculate_total()

    assert result == 100
    assert "calculate_total executed in" in caplog.text


def test_decorator_preserves_metadata():
    @measure_execution_time
    def calculate_total():
        return 100

    assert calculate_total.__name__ == "calculate_total"


def test_decorator_returns_result():
    @measure_execution_time
    def add(a: int, b: int) -> int:
        return a + b

    assert add(10, 20) == 30


def test_decorator_logs_on_exception(caplog):
    @measure_execution_time
    def divide(a: int, b: int) -> float:
        return a / b

    with caplog.at_level(logging.DEBUG):
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)

    assert "divide executed in" in caplog.text


def test_decorator_accepts_keyword_arguments():
    @measure_execution_time
    def calculate_total(a: int, b: int) -> int:
        return a + b

    assert calculate_total(a=10, b=20) == 30