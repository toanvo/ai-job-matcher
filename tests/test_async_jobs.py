import pytest

from job_matcher.async_jobs import fetch_job, fetch_jobs_sequentially, fetch_jobs_concurrently


@pytest.mark.asyncio
async def test_fetch_job() -> None:
    result = await fetch_job("LinkedIn", 0)

    assert result == "Job retrieved from LinkedIn"


@pytest.mark.asyncio
async def test_fetch_jobs_sequentially() -> None:
    result = await fetch_jobs_sequentially()    

    assert result == ['Job retrieved from Linked', 'Job retrieved from Indeed', 'Job retrieved from SEEK']


@pytest.mark.asyncio
async def test_fetch_jobs_concurrently() -> None:
    result = await fetch_jobs_concurrently()

    assert result == ['Job retrieved from Linked', 'Job retrieved from Indeed', 'Job retrieved from SEEK']