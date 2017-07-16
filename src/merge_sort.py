"""A merge sort function."""


def merge_sort(numbers):
    """Sort a iterable of numbers into min first via merge sort."""
    temp = []
    if len(numbers) % 2 == 0:
        for i in range(0, len(numbers), 2):
            temp.append(numbers[i: i + 2])
        for pair in temp:
            if pair[0] > pair[1]:
                pair[0], pair[1] = pair[1], pair[0]

    return temp
