from typing import Protocol
from .models import Job


class JobMatchingStrategy(Protocol):
    def calculate_match(
            self,
            job: Job,
            skills: set[str]
    ) -> float:
        ...

