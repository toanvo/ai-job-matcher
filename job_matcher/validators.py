from .models import Job
from .exceptions import InvalidJobError


def validate_job(job: Job) -> None:
    if not isinstance(job, dict):
        raise InvalidJobError("The job must be a dictionary type")

    if "title" in job:
        if not isinstance(job["title"], str):
            raise InvalidJobError("The job title must be a string type")
    
    if "skills" in job:
        skills = job["skills"]
        if not isinstance(skills, list):
            raise InvalidJobError("The job skills must be a list of strings")

        for skill in skills:
            if not isinstance(skill, str):
                raise InvalidJobError("The skill must be a string")
    