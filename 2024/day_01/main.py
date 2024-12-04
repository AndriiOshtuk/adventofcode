import pathlib
import pytest
from collections import Counter

INPUT_FILE = pathlib.Path(__file__).parent / 'input.csv'


def get_total_distance(file: str):
    side_a = []
    side_b = []

    for line in file.splitlines():
        a,b = line.split()
        side_a.append(int(a))
        side_b.append(int(b))

    side_a = sorted(side_a)
    side_b = sorted(side_b)

    sum = 0
    for i in range(len(side_a)):
        sum += abs(side_a[i] - side_b[i])
    
    return sum


def get_similarity_score(file: str):
    side_a = []
    side_b = []

    for line in file.splitlines():
        a,b = line.split()
        side_a.append(int(a))
        side_b.append(int(b))

    multipliers = Counter(side_b)
    result = 0
    for v in side_a:
        result += v * multipliers[v]
    return result


if __name__ == "__main__":
    with open(INPUT_FILE, mode="r") as f:
        file = f.read()
        print("Day1 (Part 1): What is the total distance between your lists?")
        result = get_total_distance(file)
        print(f"Result={result}")
        print("\nDay1 (Part 2): Calculate a total similarity score")
        result = get_similarity_score(file)
        print(f"Result={result}")


TEST_INPUT = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUT, 11),
    ),
)
def test_get_total_distance(input_s, expected):
    actual = get_total_distance(input_s)
    assert actual == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUT, 31),
    ),
)
def test_get_similarity_score(input_s, expected):
    actual = get_similarity_score(input_s)
    assert actual == expected