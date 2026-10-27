from .models import Job
from .validators import validate_job

class KeywordMatcher:
    def calculate_match(
            self,
            job: Job,
            skills: set[str]
    ) -> float:
        validate_job(job)

        required = {
            skill.strip().casefold() 
            for skill in job.get("skills", [])
        }
        candidate = {
            current_skill.strip().casefold() 
            for current_skill in skills
        }

        if not required:
            return 0.0
    
        matched = required & candidate
        return 100.0 if matched else 0.0