import inspect, pytest
from job_matcher.matching import JobMatcher
from job_matcher.exceptions import InvalidJobError


def test_iter_matching_jobs_returns_expected_results():
    matcher = JobMatcher(threshold=50.0)

    jobs = [
        {"title": "Python Developer", "skills": ["Python", "Docker"]},
        {"title": "Java Developer", "skills": ["Java", "Spring"]},
        {"title": "AI Engineer", "skills": ["Python", "Azure", "LLM"]},
    ]

    result = list(
        matcher.iter_matching_jobs(jobs, {"Python", "Azure"})
    )

    assert [job.title for job in result] == [
        "Python Developer",
        "AI Engineer"
    ]

    assert [job.score for job in result] == [
        50.0,
        66.67
    ]

def test_iter_matching_jobs_returns_generator():
    matcher = JobMatcher()

    jobs = [
        {"title": "Python Developer", "skills": ["Python"]},
    ]

    result = matcher.iter_matching_jobs(jobs, {"Python"})

    assert inspect.isgenerator(result)

def test_iter_matching_jobs_is_lazy():
    matcher = JobMatcher(threshold=50.0)

    jobs = [
        {"title": "Python Developer", "skills": ["Python"]},
        {"title": "Invalid Job", "skills": None},
    ]

    generator = matcher.iter_matching_jobs(jobs, {"Python"})

    # Step 1: Request the first result.
    first = next(generator)

    assert first.title == "Python Developer"

    # Step 2: Request the second result.
    # The second job is invalid.
    # Assert that InvalidJobError is raised.
    with pytest.raises(InvalidJobError):
        next(generator)