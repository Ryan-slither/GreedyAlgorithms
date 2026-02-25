from random import randint

from src.data import InputData


def generate_test_input(
    cache_size: int, requests_count: int, unique_requests: int
) -> InputData:
    return InputData(
        cache_size,
        requests_count,
        [randint(1, unique_requests) for _ in range(requests_count)],
    )
