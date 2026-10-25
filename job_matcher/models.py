from dataclasses import dataclass
from typing import TypedDict, NotRequired


class Job(TypedDict):
    title: NotRequired[str]
    skills: NotRequired[list[str]]

@dataclass
class MatchedJob:
    title: str
    score: float   

    def __str__(self) -> str:
        return f"{self.title}: {self.score}% match"

        