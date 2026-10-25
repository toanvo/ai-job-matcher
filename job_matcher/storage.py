import json
from pathlib import Path

from .models import Job
from .validators import validate_job
from typing import Union


def load_jobs(filepath: Union[str, Path]) -> list[Job]:
    path = Path(filepath)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    
    if not isinstance(data, list):
        raise ValueError("Job data must be a list")

    for job in data:
        validate_job(job)

    return data

