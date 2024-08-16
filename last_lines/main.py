import io
from pathlib import Path


def last_lines(filename: str, buffer_size: int = io.DEFAULT_BUFFER_SIZE) -> iter:
    """
    Generator function to yield the lines of a file in reverse order.

    Args:
        :param filename: The path to the file.
        :param buffer_size: The buffer size to use when reading the file. Defaults to io.DEFAULT_BUFFER_SIZE.

    Yields:
        :return iter: Lines of the file in reverse order.
    """
    with open(
        Path(filename),
        "r",
        buffering=buffer_size,
        encoding="utf-8",
    ) as file:
        for line in reversed(file.readlines()):
            yield line
