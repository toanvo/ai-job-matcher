import logging
from job_matcher import match_jobs
from job_matcher.matching import JobMatcher
from job_matcher.context_managers import measure_block
from job_matcher.matching_service import JobMatchingService
from job_matcher.strategies import KeywordMatcher

def main() -> None:
    jobs = [
        {
            "title": "Senior Python Developer",
            "skills": ["Python", "FastAPI", "Docker"]
        },
        {
            "title": "Senior .NET Developer",
            "skills": ["C#", ".NET", "Azure"]
        },
        {
            "title": "AI Engineer",
            "skills": ["PYthon", "LLM", "Azure"]
        },
        {
            "title": "Python Developer",
            "skills": ["PYthon", "python", "PYTHON", "Database", "Odoo"]
        }
    ]
    
    my_skills = {"python", "Azure", "Docker"}
    percentage_service = JobMatchingService(JobMatcher())
    keyword_service = JobMatchingService(KeywordMatcher())

    print(" Percentage matcher: ")
    for job in percentage_service.match_jobs(jobs, my_skills):
        print(job)

    print("Keyword service: ")
    for job in keyword_service.match_jobs(jobs, my_skills):
        print(job)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s | %(name)s | %(message)s",
    )

    main()