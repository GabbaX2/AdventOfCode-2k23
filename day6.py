from typing import List
from functools import reduce

def parse_values(line: str) -> List[int]:
    _, *nums_str = line.split()
    return list(map(int, nums_str))

def calculate_margin(time: int, record: int) -> int:
    return sum(1 for i in range(time + 1) if i * (time - i) > record)

def main():
    with open('day6.in', 'r') as handle:
        time_str, distance_str = handle.read().splitlines()

    times = parse_values(time_str)
    distances = parse_values(distance_str)
    margins = map(calculate_margin, times, distances)

    print(reduce(lambda a, b: a * b, margins))

if __name__ == '__main__':
    main()
