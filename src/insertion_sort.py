"""An example of the insertion sort."""


def insertion_sort(numbers):
    """Will sort any given number iterable into a min first list."""
    new = []
    while len(new) < len(numbers):
        x = 0
        for i in numbers:
            while True:
                try:
                    if new[x] >= i:
                        new.insert(x, i)
                        x = 0
                        break
                    else:
                        x += 1
                except IndexError:
                    new.append(i)
                    x = 0
                    break
    return new
