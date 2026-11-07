import pytest

from job_matcher.async_task_service import (
    fetch_jobs_with_tasks,
    fetch_job_with_timeout,
    cancel_job_fetch,
    fetch_jobs_with_error_handling,
)


@pytest.mark.asyncio
async def test_fetch_jobs_with_tasks() -> None:
    results = await fetch_jobs_with_tasks()

    assert len(results) == 3
    assert results == [
        "Job retrieved from LinkedIn",
        "Job retrieved from Indeed",
        "Job retrieved from SEEK",
    ]


@pytest.mark.asyncio
async def test_fetch_job_with_timeout_success() -> None:
    result = await fetch_job_with_timeout(
        "LinkedIn",
        delay=0,
        timeout=1.0
    )

    assert result == "Job retrieved from LinkedIn"


@pytest.mark.asyncio
async def test_fetch_job_with_timeout_failure() -> None:
    result = await fetch_job_with_timeout(
        "LinkedIn",
        delay=1.0,
        timeout=0.01
    )

    assert result == "Timeout retrieving jobs from LinkedIn"


@pytest.mark.asyncio
async def test_cancel_job_fetch() -> None:
    result = await cancel_job_fetch()

    assert result == "Job retrieval cancelled"

@pytest.mark.asyncio
async def test_fetch_jobs_with_error_handling() -> None:
    result = await fetch_jobs_with_error_handling()

    assert result == [
        'Job retrieved from LinkedIn',
        'Indeed failed: Indeed API unavailable',
        'Job retrieved from SEEK'
    ]