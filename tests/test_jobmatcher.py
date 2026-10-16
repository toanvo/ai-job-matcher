import pytest
from job_matcher import calculate_match, match_jobs, MatchedJob

@pytest.mark.parametrize(
    "job, skills, expected",
    [
        (
            {"title": "All Skills", "skills": ["Python", "Azure"]},
            {"Python", "Azure"},
            100.0
        ),
        (
            {"title": "Partial Match", "skills": ["Python", "Docker"]},
            {"Python"},
            50.0
        ),
        (
            {"title": "No Match", "skills": ["Java", "Spring"]},
            {"Python"},
            0.0
        ),
        (
            {"title": "Empty Skills", "skills": []},
            {"Python"},
            0.0
        ),
        (
            {"title": "Missing Skills"},
            {"Python"},
            0.0
        ),
        (
            {"title": "Case Insensitive", "skills": ["PYTHON"]},
            {"python"},
            100.0
        ),
        (
            {"title": "Whitespace", "skills": [" Python "]},
            {" python "},
            100.0
        ),
        (
            {"title": "Duplicates", "skills": ["Python", "PYTHON"]},
            {"python"},
            100.0
        )
    ]
)
def test_calculate_match(job, skills, expected):
    result = calculate_match(job, skills)

    assert result == expected

@pytest.mark.parametrize(
    "jobs, skills, expected",
    [
        (
            [
                {
                    "title": "All Skills", 
                    "skills": ["Python", "Azure"]
                },
                {
                    "title": "All Skills 2", 
                    "skills": ["Python", "Azure"]
                }
            ],
            {"Python", "Azure"},
            [
                MatchedJob("All Skills", 100.0),
                MatchedJob("All Skills 2", 100.0)
            ]
        ),
        (
            [{"title": "Partial Match", "skills": ["Python", "Docker", "Database", "Pytorch"]}],
            {"Python", "Database", "Docker"},
            [MatchedJob("Partial Match", 75.0)]
        ),
        (
            [{"title": "No Match", "skills": ["Java", "Spring"]}],
            {"Python"},
            []
        ),
        (
            [{"title": "Empty Skills", "skills": []}],
            {"Python"},
            []
        ),
        (
            [{"title": "Missing Skills"}],
            {"Python"},
            []
        ),
        (
            [{"title": "Case Insensitive", "skills": ["PYTHON"]}],
            {"python"},
            [MatchedJob("Case Insensitive", 100.0)]
        ),
        (
            [{"title": "Whitespace", "skills": [" Python "]}],
            {" python "},
            [MatchedJob("Whitespace", 100.0)]
        ),
        (
            [{"title": "Duplicates", "skills": ["Python", "PYTHON"]}],
            {"python"},
            [MatchedJob("Duplicates", 100.0)]
        )
    ]
)
def test_match_jobs_returns_expected_results(jobs, skills, expected):    
    result = match_jobs(jobs, skills)    
    assert result == expected

def test_match_jobs_sorted_descending():
    jobs = [
        {"title": "50% Match", "skills": ["Python", "Docker"]},
        {"title": "100% Match", "skills": ["Python"]},
        {"title": "0% Match", "skills": ["Java"]},
    ]

    result = match_jobs(jobs, {"Python"})

    assert [job.title for job in result] == [
        "100% Match",
        "50% Match"    
    ]