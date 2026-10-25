import pytest

from job_matcher.validators import validate_job
from job_matcher.exceptions import InvalidJobError


@pytest.mark.parametrize(
    "job",
    [
        {"title": "AI Engineer", "skills": ["Python"]},
        {"title": "AI Engineer", "skills": []},
        {},
        {"skills": ["Python", "Azure"]},
    ],
)
def test_valid_job(job):
    assert validate_job(job) is None


@pytest.mark.parametrize(
    "job",
    [
        None,
        "AI Engineer",
        {"title": 123},
        {"skills": None},
        {"skills": "Python"},
        {"skills": [123]},
        {"skills": ["Python", None]},
    ],
)
def test_invalid_job(job):
    with pytest.raises(InvalidJobError):
        validate_job(job)