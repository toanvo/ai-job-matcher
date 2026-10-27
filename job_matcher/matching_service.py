from .job_matching_strategy import JobMatchingStrategy
from .models import Job, MatchedJob


class JobMatchingService():
    def __init__(self, matcher: JobMatchingStrategy):
        self.matcher = matcher

    def match_jobs(
            self,
            jobs: list[Job],
            skills: set[str]
    ) -> list[MatchedJob]:
        matched_jobs : list[MatchedJob] = []
    
        for job in jobs:
            score = self.matcher.calculate_match(job, skills)
            if score >= 50.0:
                matched_jobs.append(
                    MatchedJob(job.get("title", ""), score)
                )

        return sorted(
            matched_jobs,
            key = lambda job: job.score,
            reverse=True
        )

