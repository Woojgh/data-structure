"""Test radixsort."""
import pytest
from random import randint
from radix_sort import radix_sort


def test_radix_non_list_raises_error():
    """Entering a non-list/tuple param raises an error."""
    with pytest.raises(TypeError):
        radix_sort('Hello')


def test_radix_non_int_raises_error():
    """Entering an iterable containing non-integers raises an error."""
    with pytest.raises(ValueError):
        radix_sort([1, 2, 3, 5, 'burp'])


@pytest.mark.parametrize('input, expected', to_sort)
def test_radix_sort_returns_ordered_list(input, expected):
    """Radix sort returns an ordered list."""
    assert radix_sort(input) == expected


def test_radix_sort_sorts_random_list():
    """Radix sort returns an ordered list."""
    input = [randint(0, 1000) for i in range(100)]
    expected = sorted(input)
    assert radix_sort(input) == expected