import os

from src.data import InputData, OutputData
from src.generate import generate_test_input
from src.input_output import (
    read_input_file,
    read_output_file,
    write_input_file,
    write_output_file,
)

if __name__ == "__main__":
    print(read_input_file("data/input.in"))
    print(read_output_file("data/output.in"))

    output_file_name = "data/output_test.in"
    write_output_file(output_file_name, OutputData(5, 5, 5))
    print(read_output_file(output_file_name))
    os.remove(output_file_name)

    input_file_name = "data/input_test.in"
    write_input_file(input_file_name, InputData(5, 5, [5, 5, 5, 5, 5]))
    print(read_input_file(input_file_name))
    os.remove(input_file_name)

    print(generate_test_input(6, 67, 10))
