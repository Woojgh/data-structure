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


def existing_set_insertion_sort(numbers, existing_set):
    """Will sort any given number iterable into a min first list."""
    new = list(existing_set)
    while len(new) < len(numbers) + len(existing_set):
        x = 0
        for i in numbers:
            while True:
                try:
                    if x is 0 and new[x] >= i:
                        new.insert(x, i)
                        break
                    elif new[x] >= i:
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
