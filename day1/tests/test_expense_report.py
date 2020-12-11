"""
Test the
"""
from day1.expense_report import find_2020

TEST_DATA = [2000, 1000, 20]


def test_find_2020():
    expected_result = 40000
    actual_result = find_2020(TEST_DATA)
    assert expected_result == actual_result


if __name__ == '__main__':
    pass
