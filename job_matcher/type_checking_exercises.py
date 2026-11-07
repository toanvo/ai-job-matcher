from job_matcher.job_matching_strategy import JobMatchingStrategy
from job_matcher.matching import JobMatcher
from job_matcher.strategies import KeywordMatcher
from job_matcher.matching_service import JobMatchingService 
from job_matcher.results import Result


class InvalidMatcher:
    def calculate_match(
        self,
        job:str,
        skills: list[str]
    ) -> str:
        return "75%"


class InvalidDependency:
    def calculate_match(
        self,
        job:str,
        skills: list[str]
    ) -> str:
        return "invalid"


def print_skills(result: Result[list[str]]) -> None:
    if result.data is None:
        print("No skills available")
        return
    print(len(result.data))


def use_matcher(matcher: JobMatchingStrategy) -> None: 
    print(type(matcher).__name__)


use_matcher(JobMatcher())
use_matcher(KeywordMatcher())
# use_matcher(InvalidMatcher())

percentage_service = JobMatchingService(JobMatcher())
keyword_service = JobMatchingService(KeywordMatcher())
# invalid_service = JobMatchingService(InvalidDependency())

