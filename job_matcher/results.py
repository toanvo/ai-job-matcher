from dataclasses import dataclass

@dataclass
class Result[T]:
    data: T | None = None
    error: str | None = None

    @property
    def is_success(self) -> bool:
        return self.error is None