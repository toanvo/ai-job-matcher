from dataclasses import dataclass
from typing import TypedDict
from typing_extensions import NotRequired

class Job(TypedDict):
    title: NotRequired[str]
    skills: NotRequired[list[str]]

@dataclass
class MatchedJob:
    title: str
    score: float

    def __str__(self) -> str:
        return f"{self.title}: {self.score}% match"

def calculate_match(job: Job, skills: set[str]) -> float:
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

def match_jobs(jobs: list[Job], skills: set[str]) -> list[MatchedJob]:
    matched_jobs: list[MatchedJob] = []

    for job in jobs:
        score = calculate_match(job, skills)
        if score >= 50.0:
            matched_jobs.append(
                MatchedJob(job.get("title", ""), score)
            )

    return sorted(
        matched_jobs, 
        key=lambda mj: mj.score, 
        reverse=True
    )

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


    test_cases = [
        {"title": "Empty Skills", "skills": []},
        {"title": "Missing Skills"},
        {"title": "Whitespace", "skills": [" Python "]},
        {"title": "Duplicates", "skills": ["Python", "PYTHON"]},
    ]
    x_skills = {" python ", "Azure"}    
    my_skills = {"python", "Azure", "Docker"}
    my_matched_jobs = match_jobs(test_cases, x_skills)
    
    # my_matched_jobs = match_jobs(jobs, my_skills)

    for mj in my_matched_jobs:
        print(mj)

if __name__ == "__main__":
    main()