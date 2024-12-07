import pathlib
import pytest
from itertools import count


INPUT_FILE = pathlib.Path(__file__).parent / 'input.csv'

def is_report_safe(report: list[int]) -> bool:
    if not report:
        return False
    
    asc = True if (report[1] - report[0]) > 0 else False

    for i in range(len(report)-1):
        if asc:
            diff = report[i+1] - report[i]
        else:
            diff = report[i] - report[i+1]
        
        if diff < 1 or diff > 3:
            return False
        
    return True


def get_safe_reports_quantity(file: str) -> int:
    safe_reports = 0
    for line in file.splitlines():
        report = list(map(int, line.split()))
        if is_report_safe(report):
            safe_reports += 1
    return safe_reports


def get_safe_reports_quantity_with_dampener(file: str) -> bool:
    safe_reports = 0
    for line in file.splitlines():
        report = list(map(int, line.split()))
        if is_report_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                sub_report = report[:]
                sub_report.pop(i)
                safe = is_report_safe(sub_report)
                if safe:
                    safe_reports += 1
                    break
    return safe_reports


if __name__ == "__main__":
    with open(INPUT_FILE, mode="r") as f:
        file = f.read()
        print("Day2 (Part 1): Safe reports")
        result = get_safe_reports_quantity(file)
        print(f"Result={result}")
        print("\nDay2 (Part 2): Safe reports (if can skip one 'bad' level)")
        result = get_safe_reports_quantity_with_dampener(file)
        print(f"Result={result}")


TEST_INPUT = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUT, 2),
    ),
)
def test_get_safe_reports_quantity(input_s, expected):
    actual = get_safe_reports_quantity(input_s)
    assert actual == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUT, 4),
        ("1 2 2 2 3", 0),
        ("1 2 1 3 3", 0),
        ("21 22 25", 1),
    ),
)
def test_get_safe_reports_quantity_with_dampener(input_s, expected):
    actual = get_safe_reports_quantity_with_dampener(input_s)
    assert actual == expected
