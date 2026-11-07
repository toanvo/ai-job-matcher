import asyncio
import time


async def fetch_job(source: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Job retrieved from {source}"


async def fetch_jobs_sequentially() -> list[str]:
    sources = ["Linked", "Indeed", "SEEK"]
    results: list[str] = []
    for source in sources:
        result = await fetch_job(source, 1.0)
        results.append(result)
    
    return results


async def fetch_jobs_concurrently() -> list[str]:
    sources = ["Linked", "Indeed", "SEEK"]    

    results = await asyncio.gather(
        *(fetch_job(source, 1.0) for source in sources)
    )
    
    return list(results)


async def main() -> None:
    start = time.perf_counter()
    
    results = await fetch_jobs_concurrently()

    duration = time.perf_counter() - start

    print(results)
    print(f"Execution time: {duration:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())