#!/usr/bin/python3
"""" returns a list of lists of integers"""


def pascal_triangle(n):
    result = []
    if n <= 0:
        return result

    last = [1]
    for i in range(1, n + 1):
        actual = [1] * i
        actual = [last[index - 1] + last[index] if index > 0 and
                  index < len(actual) - 1 else 1 for index,
                  value in enumerate(actual)]
        last = actual
        result.append(actual)
    return