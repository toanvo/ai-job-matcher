import pytest
from job_matcher.matching_service import JobMatchingService
from job_matcher.models import Job


class FakeMatcher:
    def calculate_match(
        self,
        job: Job,
        skills: set[str]
    ) -> float:
        scores = {
            "Python Developer": 75.0,
            "Java Developer": 30.0,
            "AI Engineer": 90.0
        }

        return scores.get(job.get("title", ""), 0.0)



@pytest.mark.parametrize(
    "jobs, skills",
    [
        (
            [                  
                {"title": "Python Developer", "skills": ["Python", "Azure"]},                
                {"title": "Python Developer", "skills": [" PYTHON "]}                
            ],
            {"python"}
        )        
    ]
)
def test_service_with_fake_matcher(jobs, skills):    
    
    fake_mather = JobMatchingService(FakeMatcher())    
    matched_jobs = fake_mather.match_jobs(jobs,skills)
   
    assert len(matched_jobs) == 2

    for matched_job in matched_jobs:
        assert matched_job.score == 75.0

@pytest.mark.parametrize(
    "jobs, skills",
    [
        (
            [
                {
                    "title": "Python Developer",
                    "skills": ["Python", "Azure", "Docker", "Postgresql"]
                },
                {
                    "title": "Java Developer",
                    "skills": ["Java", "Oracle", "Python"]
                },
                {
                    "title": "AI Engineer",
                    "skills": ["Python", "Azure", "Docker"]
                }
            ],
            {"python", "azure", "docker"}
        )
    ]
)
def test_service_filters_low_scores(jobs, skills):
    service = JobMatchingService(FakeMatcher())

    matched_jobs = service.match_jobs(jobs, skills)

    assert len(matched_jobs) == 2

    assert matched_jobs[0].score == 90.0
    assert matched_jobs[0].title == "AI Engineer"

    assert matched_jobs[1].score == 75.0
    assert matched_jobs[1].title == "Python Developer"

    assert all(
        job.title != "Java Developer"
        for job in matched_jobs
    )

    