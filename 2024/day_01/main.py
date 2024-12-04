import pathlib
import pytest

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


if __name__ == "__main__":
    print("Day1 (Part 1): What is the total distance between your lists?")

    with open(INPUT_FILE, mode="r") as f:
        result = get_total_distance(f.read())
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