import pytest
from unittest.mock import Mock, call

from job_matcher.matching_service import JobMatchingService


def test_service_calls_matcher_once():
    job = {
        "title": "Python developer",
        "skills": ["Python", "Azure"]
    }

    skills = {"Python"}
    matcher = Mock()

    matcher.calculate_match.return_value = 75.0
    service = JobMatchingService(matcher)
    result = service.match_jobs([job], skills)
    matcher.calculate_match.assert_called_once_with(job, skills)
    assert len(result) == 1
    assert result[0].title == "Python developer"
    assert result[0].score == 75.0

def test_service_calls_matcher_for_each_job():
    jobs = [
        {"title": "Python Developer", "skills": ["Python"]},
        {"title": "AI Engineer", "skills": ["Azure"]},
        {"title": "Java Developer", "skills": ["Java"]}
    ]

    skills = {"Python"}

    matcher = Mock()

    matcher.calculate_match.side_effect = [
        75.0,
        90.0,
        30.0
    ]

    service = JobMatchingService(matcher)
    result = service.match_jobs(jobs, skills)
    assert matcher.calculate_match.call_count == 3
    assert len(result) == 2
    assert matcher.calculate_match.call_args_list == [
        call(jobs[0], skills),
        call(jobs[1], skills),
        call(jobs[2], skills)
    ]
    assert result[0].title == "AI Engineer"
    assert result[0].score == 90.0

    assert result[1].title == "Python Developer"
    assert result[1].score == 75.0

def test_service_propagates_matcher_exception():
    matcher = Mock()

    matcher.calculate_match.side_effect = RuntimeError(
        "Matching engine unavailable"
    )

    service = JobMatchingService(matcher)

    jobs = [
        {"title": "Python Developer", "skills": ["Python"]}
    ]

    skills = {"Python"}

    with pytest.raises(RuntimeError, match="Matching engine unavailable"):
        service.match_jobs(jobs, skills)

    assert matcher.calculate_match.call_count == 1
    matcher.calculate_match.assert_called_once_with(
        jobs[0],
        skills
    )
    