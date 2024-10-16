import time
import typing
from random import randint


def quadratic_solution(arr: typing.List[int]) -> int:
    max_sum: int = 0
    for i in range(len(arr)):
        current_sum = arr[i]
        max_sum = max(max_sum, current_sum)
        for j in range(i + 1, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


def linear_solution(arr: typing.List[int]) -> int:
    max_sum = 0
    current_sum = 0
    first_item = True
    for element in arr:
        if first_item:
            current_sum = element
            max_sum = element
            first_item = False
            continue
        current_sum = max(current_sum + element, element)
        max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    data_sizes: list = [10, 100, 1000, 10000, 100000]
    for data_size in data_sizes:
        data: list = [randint(-100, 100) for _ in range(data_size)]

        start_time = time.perf_counter()
        result = quadratic_solution(data)
        elapsed_time = time.perf_counter() - start_time
        print(f'Quadratic solution. Data size: {data_size} Result: {result} Time: {elapsed_time:8f}')

        start_time = time.perf_counter()
        result = linear_solution(data)
        elapsed_time = time.perf_counter() - start_time
        print(f'Linear solution. Data size: {data_size} Result: {result} Time: {elapsed_time:8f}')


if __name__ == '__main__':
    main()
