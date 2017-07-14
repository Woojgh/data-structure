"""An example of the basic bubble sort function."""


def bubble_sort(numbers):
    """Basic bubble sort."""
    sorted_numbers = list(numbers)
    count = 0
    while count < len(sorted_numbers) - 1:
        count = 0
        for x in range(len(sorted_numbers) - 1):
            if sorted_numbers[x] > sorted_numbers[(x + 1)]:
                sorted_numbers[x], sorted_numbers[x + 1] = sorted_numbers[x + 1], sorted_numbers[x]
            else:
                count += 1
    return sorted_numbers
