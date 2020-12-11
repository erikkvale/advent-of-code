"""
Main test
"""


def find_2020(expense_report: list):
    while expense_report:
        current_key = expense_report.pop(0)
        for entry in expense_report:
            if (current_key + entry) == 2020:
                return (current_key, entry)
            else:
                continue
    return None


if __name__ == '__main__':
    with open("data.txt", 'r') as f:
        data = [int(l.strip()) for l in f.readlines()]
    find_2020(data)