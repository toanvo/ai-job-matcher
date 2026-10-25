import pytest
from job_matcher.matching import JobMatcher
from job_matcher.exceptions import InvalidJobError


def test_default_threshold():
    matcher = JobMatcher()

    assert matcher.threshold == 50.0


def test_custom_threshold():
    matcher = JobMatcher(80.0)

    assert matcher.threshold == 80.0


def test_threshold_can_be_updated():
    matcher = JobMatcher()

    matcher.threshold = 90.0

    assert matcher.threshold == 90.0


def test_invalid_threshold_preserves_existing_value():
    matcher = JobMatcher(75.0)

    with pytest.raises(ValueError):
        matcher.threshold = 150.0

    assert matcher.threshold == 75.0


@pytest.mark.parametrize(
    "threshold",
    [-1.0, 101.0]
)
def test_invalid_threshold(threshold):
    with pytest.raises(ValueError):
        JobMatcher(threshold)


def test_custom_threshold_filters_jobs():
    matcher = JobMatcher(75.0)

    jobs = [
        {"title": "Full Match", "skills": ["Python"]},
        {"title": "Partial Match", "skills": ["Python", "Docker"]}
    ]
    result = matcher.match_jobs(jobs, {"Python"})

    assert [job.title for job in result] == ["Full Match"]


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
    matcher = JobMatcher()
    with pytest.raises(InvalidJobError):
        matcher.calculate_match(job, {"Python"})
    