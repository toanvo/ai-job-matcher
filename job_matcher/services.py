from .models import Job, MatchedJob
from .matching import match_jobs
from .results import Result
from .exceptions import InvalidJobError


def match_job_safe(
        jobs: list[Job],
        skills : set[str]        
) -> Result[list[MatchedJob]]:
    try:    
        matched_jobs = match_jobs(jobs, skills)
        return Result(data=matched_jobs)
    except InvalidJobError as e:
        return Result(error=str(e))
    
