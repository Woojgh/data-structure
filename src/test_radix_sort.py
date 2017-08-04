"""Test radixsort."""
import pytest
from random import randint
from radix_sort import radix_sort

to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
]


# def test_radix_non_list_raises_error():
#     """Entering a non-list/tuple param raises an error."""
#     with pytest.raises(TypeError):
#         radix_sort('Monkies')


# def test_radix_non_int_raises_error():
#     """Entering an iterable containing non-integers raises an error."""
#     with pytest.raises(ValueError):
#         radix_sort([1, 2, 3, 'Nah man', 5])


@pytest.mark.parametrize('input, output', to_sort)
def test_radix_sort_returns_ordered_list(input, output):
    """Radix sort returns an ordered list."""
    assert radix_sort(input) == output


def test_radix_sort_sorts_random_list():
    """Radix sort returns an ordered list."""
    input = [randint(0, 1000) for i in range(100)]
    output = sorted(input)
    assert radix_sort(input) == output
