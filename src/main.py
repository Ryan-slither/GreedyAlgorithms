from src.algorithm import fifo, lru, optff
from src.input_output import (
    read_input_file,
)

if __name__ == "__main__":
    # input1 = read_input_file("data/input.in")

    # fifo_result = fifo(input1)
    # print(fifo_result)

    # lru_result = lru(input1)
    # print(lru_result)

    # optff_result = optff(input1)
    # print(optff_result)

    # input2 = read_input_file("data/input2.in")

    # fifo_result = fifo(input2)
    # print(fifo_result)

    # lru_result = lru(input2)
    # print(lru_result)

    # optff_result = optff(input2)
    # print(optff_result)

    input3 = read_input_file("data/input3.in")

    optff_result = optff(input3)
    print(optff_result)
