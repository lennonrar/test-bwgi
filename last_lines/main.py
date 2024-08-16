import io
from pathlib import Path


def last_lines(filename: str, buffer_size: int = io.DEFAULT_BUFFER_SIZE) -> iter:
    with open(
        Path(filename),
        "r",
        buffering=buffer_size,
        encoding="utf-8",
    ) as file:
        for line in reversed(file.readlines()):
            yield line
