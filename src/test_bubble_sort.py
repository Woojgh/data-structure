"""Will test the bubble sort for desired outputs."""
from bubble_sort import bubble_sort
import random


def test_bubble_sort():
    """Test against many random outputs."""
    assert bubble_sort(random.sample(range(100), 100)) == list(range(100))
    assert bubble_sort(random.sample(range(100), 100)) == list(range(100))
    assert bubble_sort(random.sample(range(100), 100)) == list(range(100))
    assert bubble_sort(random.sample(range(100), 100)) == list(range(100))
    assert bubble_sort(random.sample(range(100), 100)) == list(range(100))
