# GreedyAlgorithms

Programming Assignment 2

## Setup

Ryan Froug 83197825

**Must use Python version 3.14+**

1. Create virtual environment: `python -m venv .venv`
2. Start virtual environment: `.venv/scripts/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Run main: `python -m src.main`

## Questions

### Question 1

| Input File  | k   | m   | FIFO | LRU | OPTFF |
| ----------- | --- | --- | ---- | --- | ----- |
| Q1Input1.in | 10  | 100 | 32   | 39  | 23    |
| Q1Input2.in | 10  | 200 | 62   | 59  | 33    |
| Q1Input3.in | 10  | 400 | 143  | 141 | 68    |

OPTFF has the least amount of misses. It seems like FIFO and LRU are quite similar in the number of misses, but LRU has a slightly lower miss rate.

### Question 2

#### Input

```
3 14
1 2 3 4 5 6 2 1 6 5 4 3 2 1
```

#### Output

```
FIFO : 13
LRU : 13
OPTFF : 9
```

The following sequence produces a case where OPTFF performs strictly better than
FIFO and LRU. This is because there are many unique requests that do not occur very
often compared to, as in the example, 1 and 2. This allows OPTFF to consistently store these values while evicting others, so there are much fewer misses.

### Question 3

Let O be the schedule for OPTFF and A be the schedule for ( A ). O will have no larger misses than that of A over some request sequence r<sub>1</sub>, r<sub>2</sub>, ..., r<sub>i</sub>.

For the amount of requests up to the cache size k, the schedules will agree by simply placing the request into the caches. Once an eviction must occur differences will begin. At some time t, the first difference occurs at a request r<sub>t</sub>.

Case 1: The request is already within both caches, so regardless of what A does no more misses can be incured by O.

Case 2: The request is not within the caches. A can choose to evict any request from its cache, while O will choose to evict a request that never is seen in the future or is farthest in the future compared to others. -->

Case 2a: In the case that the request is never seen again, if A does not pick it then it will never benefit because there cannot be less misses on that request. O is still no larger.

Case 2b: In the case the request is seen again, if A does pick the same as O then it can be no larger. If A picks a different request, it would be picking one requested sooner in the future than the one O picks. This would result in an extra miss when it has to add that one back to the cache, and the one it keeps, in the best case, will result in one less miss or could incur an extra miss. This overall results in that O is no larger still than A.

Continue this process until r<sub>i</sub> is processed and O will not have incurred more misses than A. []
