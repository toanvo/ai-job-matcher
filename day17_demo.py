import asyncio
import time

from job_matcher.async_task_service import fetch_jobs_with_tasks, fetch_job_with_timeout


async def main() -> None:
    start = time.perf_counter()

    results = await fetch_jobs_with_tasks()

    duration = time.perf_counter() - start

    print(results)
    print(f"Execution time: {duration:.2f}s")

    result = await fetch_job_with_timeout(
        source="LinkedIn",
        delay=5.0,
        timeout=1.0
    )

    print(result)

if __name__ == "__main__":
    asyncio.run(main())