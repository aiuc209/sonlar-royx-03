import pytest

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def check_sum(numbers):
    result = []
    for num in numbers:
        if sum_of_digits(num) % 2 == 0:
            result.append("Juft sum")
        else:
            result.append("Toq sum")
    return result

@pytest.mark.parametrize("numbers, expected", [
    ([12, 34, 56], ["Juft sum", "Juft sum", "Juft sum"]),
    ([23, 45, 67], ["Toq sum", "Toq sum", "Toq sum"]),
    ([10, 20, 30], ["Juft sum", "Juft sum", "Juft sum"]),
    ([1, 2, 3], ["Toq sum", "Toq sum", "Toq sum"]),
])

def test_check_sum(numbers, expected):
    assert check_sum(numbers) == expected
