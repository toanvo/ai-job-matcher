import asyncio

from job_matcher.async_jobs import fetch_job


async def fetch_jobs_with_tasks() -> list[str]:
    sources = ["LinkedIn", "Indeed", "SEEK"]

    tasks = [
        asyncio.create_task(fetch_job(source, 1.0))
        for source in sources
    ]

    results = await asyncio.gather(*tasks)

    return list(results)


async def fetch_job_with_timeout(source: str, delay: float, timeout: float) -> str:
    try:
        result = await asyncio.wait_for(
            fetch_job(source, delay),
            timeout = timeout
        )
        
        return result
    
    except TimeoutError:
        return f"Timeout retrieving jobs from {source}"


async def cancel_job_fetch() -> str:
    task = asyncio.create_task(
        fetch_job("LinkedIn", 5.0)
    )

    await asyncio.sleep(0.1)

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        return "Job retrieval cancelled"

    return "Job retrieval completed"


async def fetch_job_with_failure(source: str) -> str:
    await asyncio.sleep(0.1)

    if source == "Indeed":
        raise RuntimeError("Indeed API unavailable")

    return f"Job retrieved from {source}"


async def fetch_jobs_with_error_handling() -> list[str]:
    sources = ["LinkedIn", "Indeed", "SEEK"]

    results = await asyncio.gather(
        *(fetch_job_with_failure(source) for source in sources),
        return_exceptions=True
    )

    output: list[str] = []

    for source, result in zip(sources, results):
        if isinstance(result, BaseException):
            output.append(f"{source} failed: {result}")
        else:
            output.append(result)

    return output