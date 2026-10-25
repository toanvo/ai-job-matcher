import logging
from job_matcher import match_jobs
from job_matcher.matching import JobMatcher
from job_matcher.context_managers import measure_block


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
    with measure_block("Job Matching"):
        my_matched_jobs = match_jobs(jobs, my_skills)

    for mj in my_matched_jobs:
        print(mj)

    matcher = JobMatcher()

    jobs2 = [
        {"title": "Python Developer", "skills": ["Python", "Docker"]},
        {"title": "Java Developer", "skills": ["Java", "Spring"]},
        {"title": "AI Engineer", "skills": ["Python", "Azure", "LLM"]},
    ]

    my_skills = {"Python", "Azure"}
    with measure_block("Generator processing"):
        for job in matcher.iter_matching_jobs(jobs2, my_skills):
            print(job)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s | %(name)s | %(message)s",
    )

    main()