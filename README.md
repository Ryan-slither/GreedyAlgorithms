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

OPTFF definitely has the least amount of misses. It seems like FIFO and LRU
are quite similar in the number of misses, but LRU has a slightly lower miss rate.

### Question 2
