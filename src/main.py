from src.algorithm import fifo, lru, optff
from src.generate import generate_test_input
from src.input_output import OutputData, read_input_file, write_input_file

if __name__ == "__main__":
    # Question 1
    # input1 = generate_test_input(10, 100, 15)
    input1 = read_input_file("data/Q1Input1.in")
    write_input_file("data/Q1Input1.in", input1)
    output1 = OutputData(fifo(input1), lru(input1), optff(input1))
    print(output1)

    # input2 = generate_test_input(10, 200, 15)
    input2 = read_input_file("data/Q1Input2.in")
    write_input_file("data/Q1Input2.in", input2)
    output2 = OutputData(fifo(input2), lru(input2), optff(input2))
    print(output2)

    # input3 = generate_test_input(10, 400, 15)
    input3 = read_input_file("data/Q1Input3.in")
    write_input_file("data/Q1Input3.in", input3)
    output3 = OutputData(fifo(input3), lru(input3), optff(input3))
    print(output3)
