from dataclasses import dataclass


@dataclass
class InputData:
    cache_size: int
    requests_count: int
    requests: list[int]


@dataclass
class OutputData:
    FIFO_misses: int
    LRU_misses: int
    OPTFF_misses: int
