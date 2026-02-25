from src.data import InputData, OutputData


def read_input_file(file_name: str) -> InputData:
    with open(file_name, "r") as f:
        lines = f.readlines()
        cache_size, requests_count = tuple(
            map(lambda x: int(x.strip()), lines[0].split(" "))
        )
        requests = list(map(lambda x: int(x.strip()), lines[1].split(" ")))
        return InputData(cache_size, requests_count, requests)


def read_output_file(file_name: str) -> OutputData:
    with open(file_name, "r") as f:
        lines = f.readlines()
        data = tuple(map(lambda line: int(line.split(" ")[-1].strip()), lines))
        return OutputData(*data)


def write_input_file(file_name: str, data: InputData) -> None:
    with open(file_name, "w") as f:
        results = (
            f"{data.cache_size} {data.requests_count}\n{' '.join(map(lambda x: str(
                            x
                        ), data.requests))}\n"
        )
        f.write(results)


def write_output_file(file_name: str, data: OutputData) -> None:
    with open(file_name, "w") as f:
        results = f"FIFO  : {data.FIFO_misses}\nLRU   : {data.LRU_misses}\nOPTFF : {data.OPTFF_misses}\n"
        f.write(results)
