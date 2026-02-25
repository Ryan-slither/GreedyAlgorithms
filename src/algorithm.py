import heapq
from collections import deque

from src.data import DoublyLinkedList, InputData, Node


def fifo(data: InputData) -> int:
    misses = 0
    cached_requests = set()
    cache_order = deque()

    for r in data.requests:
        if r in cached_requests:
            continue

        misses += 1
        cached_requests.add(r)
        cache_order.append(r)

        if len(cached_requests) > data.cache_size:
            request = cache_order.popleft()
            cached_requests.remove(request)

        # print(cached_requests)
        # print(cache_order)

    return misses


def lru(data: InputData) -> int:
    misses = 0
    cached_requests: dict[int, Node] = dict()
    cache = DoublyLinkedList()

    for r in data.requests:
        # cache.printForward()
        # cache.printBackward()
        # print("Request:")
        # print(r, cached_requests.keys())
        # print()
        if r in cached_requests.keys():
            curr_request = cached_requests[r]
            cache.remove(curr_request)
            request = cache.append(r)
            cached_requests[r] = request
            continue

        misses += 1
        request = cache.append(r)
        cached_requests[r] = request

        # print(cached_requests.keys())
        # print()

        if len(cached_requests) > data.cache_size:
            request = cache.popLeft()
            # Value must exist because cache is not empty
            # print(request)
            del cached_requests[request.value]  # type: ignore

    return misses


def optff_inefficient(data: InputData) -> int:
    misses = 0
    cache = set()

    for index, r in enumerate(data.requests):
        if r in cache:
            continue

        misses += 1

        if len(cache) + 1 > data.cache_size:
            farthest_future = cache.copy()
            for future_r in data.requests[index + 1 :]:
                if len(farthest_future) == 1:
                    break

                if future_r in farthest_future:
                    farthest_future.remove(future_r)

            cache.remove(farthest_future.pop())

        cache.add(r)

    return misses


def optff(data: InputData) -> int:
    nextReference: dict[int, float] = dict()
    nextOccurence: dict[int, float] = dict()

    for index, r in enumerate(data.requests[::-1]):
        normal_index = len(data.requests) - 1 - index
        if r not in nextOccurence.keys():
            nextOccurence[r] = normal_index
            nextReference[normal_index] = float("inf")
        else:
            nextReference[normal_index] = nextOccurence[r]
            nextOccurence[r] = normal_index

    maxHeap: list[tuple[float, int]] = []
    misses = 0
    cache = set()

    for index, r in enumerate(data.requests):
        print(cache)
        nextOccurence[r] = nextReference[index]

        if r in cache:
            heapq.heappush_max(maxHeap, (nextReference[index], r))
            continue

        if len(cache) + 1 > data.cache_size:
            request = heapq.heappop_max(maxHeap)

            if request[1] in cache:
                cache.remove(request[1])

        if r not in cache:
            misses += 1
            cache.add(r)

        heapq.heappush_max(maxHeap, (nextReference[index], r))

    return misses
