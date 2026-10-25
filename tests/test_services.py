from job_matcher.services import match_job_safe


def test_match_jobs_safe_success():
    jobs = [{
            "title" : "Python Developer",
            "skills": ["Azure", "Python"]
    }]
    
    skills = {"Python"}
    matched_jobs = match_job_safe(jobs, skills)
    assert matched_jobs.data is not None
    assert matched_jobs.is_success is True
    assert matched_jobs.data[0].score == 50.0


def test_match_jobs_safe_invalid_job():
    jobs = [{
            "title" : "Python Developer",
            "skills": "skillb"
    }]
    
    skills = {"skill1"}
    matched_jobs = match_job_safe(jobs, skills)
    assert matched_jobs.is_success is False
    assert matched_jobs.data is None
    assert matched_jobs.error == "The job skills must be a list of strings"
    
    