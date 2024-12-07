import pathlib
import pytest
from itertools import count


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

    # "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
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



if __name__ == "__main__":
    with open(INPUT_FILE, mode="r") as f:
        file = f.read()
        print("Day3 (Part 1): Result of multiplications")
        result = get_numbers(file)
        print(f"Result={result}")
        # print("\nDay2 (Part 2): Safe reports (if can skip one 'bad' level)")
        # result = get_safe_reports_quantity_with_dampener(file)
        # print(f"Result={result}")


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