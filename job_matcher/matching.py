from collections.abc import Iterator

from .models import Job, MatchedJob
from .validators import validate_job
from .decorators import measure_execution_time


def calculate_match(job: Job, skills: set[str]) -> float:
    return JobMatcher().calculate_match(job, skills)

def match_jobs(jobs: list[Job], skills: set[str]) -> list[MatchedJob]:
    return JobMatcher().match_jobs(jobs, skills)


class JobMatcher:
    def __init__(self, threshold: float = 50.0):
        self.threshold = threshold

    @property
    def threshold(self) -> float:
        return self._threshold

    @threshold.setter
    def threshold(self, value: float) -> None:
        if not 0.0 <= value <= 100.0:
            raise ValueError("Threshold must be between 0 and 100")

        self._threshold = value
    
    def calculate_match(self, job: Job, skills: set[str]) -> float:
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
        return round(len(matched) / len(required) * 100, 2)

    @measure_execution_time
    def match_jobs(
            self,
            jobs: list[Job],
            skills: set[str]
        ) -> list[MatchedJob]:
        matched_jobs: list[MatchedJob] = [] 
        for job in jobs:           
            score = self.calculate_match(job, skills)
            if score >= self.threshold:
                matched_jobs.append(
                    MatchedJob(job.get("title", ""), score)
                )
        return sorted(
            matched_jobs,
            key = lambda job: job.score,
            reverse=True
        )

    @measure_execution_time
    def iter_matching_jobs(
                self,
                jobs: list[Job],
                skills: set[str]            
            ) -> Iterator[MatchedJob]:
    
        for job in jobs:
            score = self.calculate_match(job, skills)
            if score >= self.threshold:
                yield MatchedJob(job.get("title", ""), score)