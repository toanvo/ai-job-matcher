import pytest

from job_matcher.strategies import KeywordMatcher
from job_matcher.matching import JobMatcher
from job_matcher.exceptions import InvalidJobError
from job_matcher.job_matching_strategy import JobMatchingStrategy

@pytest.mark.parametrize(
    "jobs, skills, expected",
    [
        (
            {"title": "All Skills", "skills": ["Python", "Azure"]},
            {"Python", "Azure"},
            100.0
        ),
    ]
)
def test_keyword_match_found(jobs, skills, expected):    
    match_result = KeywordMatcher().calculate_match(jobs, skills)
    assert match_result == expected


def test_keyword_no_match():
    jobs = {
        "title": "Full-stack developer",
        "skills": ["Front-end", "Backend"]
    }

    skills = {"database"}
    matched_result = KeywordMatcher().calculate_match(jobs, skills)
    assert matched_result == 0
    
@pytest.mark.parametrize(
    "job, skills, expected",
    [
        (
            {"title": "Python Developer", "skills": ["Python", "Azure"]},
            {"python"},
            100.0
        ),
        (
            {"title": "Python Developer", "skills": [" PYTHON "]},
            {"python"},
            100.0
        ),
    ]
)
def test_keyword_case_insensitive(job, skills, expected):
    result = KeywordMatcher().calculate_match(job, skills)

    assert result == expected


@pytest.mark.parametrize(
    "job, skills",
    [
        (
            {"title": "Python Developer", "skills": "Python"},
            {"Python"}
        ),
        (
            {"title": 123, "skills": ["Python"]},
            {"Python"}
        ),
        (
            {"title": "Python Developer", "skills": [123]},
            {"Python"}
        ),
    ]
)
def test_keyword_invalid_job(job, skills):
    with pytest.raises(InvalidJobError):
        KeywordMatcher().calculate_match(job, skills)


@pytest.mark.parametrize(
    "matcher, expected",
    [
        (JobMatcher(), 50.0),
        (KeywordMatcher(), 100.0),
    ]
)
def test_matching_strategies(
    matcher: JobMatchingStrategy,
    expected: float
):
    job = {
        "title": "Python Developer",
        "skills": ["Python", "Docker"]
    }

    result = matcher.calculate_match(job, {"Python"})

    assert result == expected