import pathlib
import re
import pytest


INPUT_FILE = pathlib.Path(__file__).parent / 'input.txt'


def get_numbers(input: str):
    multiplicators: list[tuple[int, int]] = []

    expected = {
        "m":"u",
        "u":"l",
        "l":"(",
        "(":"value1",
        "value1":",",
        ",":"value2",
        "value2":")"
    }

    expect = "m"
    temp = ['','']
    for ch in input:
        if ch == expect:
            expect = expected[expect]
        elif expect.startswith("value1"):
            if ch.isdigit():
                temp[0] += ch
            elif ch == ",":
                expect = expected[","]
            else:
                expect = "m"
                temp = ['','']
        elif expect.startswith("value2"):
            if ch.isdigit():
                temp[1] += ch
            elif ch == ")":
                expect = "m"
                multiplicators.append(tuple(temp))
                temp = ['','']
            else:
                expect = "m"
                temp = ['','']
        else:
            expect = "m"
            temp = ['','']
    
    total = map(lambda a: int(a[0])*int(a[1]), multiplicators)
    return sum(total)


def get_sum_with_enabled(input: str):
    total = 0
    enabled = True
    commands = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", input)
    for cmd in commands:
        if enabled:
            if cmd == "don't()":
                enabled = False
            elif cmd.startswith("mul"):
                values = re.findall(r"[0-9]{1,3}", cmd)
                new_value = int(values[0])*int(values[1])
                total += new_value
        elif cmd == "do()":
            enabled = True
    return total



if __name__ == "__main__":
    with open(INPUT_FILE, mode="r") as f:
        file = f.read()
        print("Day3 (Part 1): Result of multiplications")
        result = get_numbers(file)
        print(f"Result={result}")
        print("\nDay3 (Part 2): Add do() and don't() commands")
        result = get_sum_with_enabled(file)
        print(f"Result= {result}")


TEST_INPUT = '''\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUT, 161),
    ), 
) 

def test_get_safe_reports_quantity(input_s, expected): #
    actual = get_numbers(input_s)
    assert actual == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 48),
    ),
)

def test_get_sum_with_enabled(input_s, expected):
    actual = get_sum_with_enabled(input_s)
    assert actual == expected