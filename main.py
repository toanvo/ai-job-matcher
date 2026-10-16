from job_matcher import match_jobs

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
    # my_matched_jobs = match_jobs(test_cases, x_skills)
    
    my_matched_jobs = match_jobs(jobs, my_skills)

    for mj in my_matched_jobs:
        print(mj)

if __name__ == "__main__":
    main()