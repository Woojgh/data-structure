"""Testings of the proper parents."""
import pytest
from proper_parents import pp


PARAMS_TABLE = [
    ('()()()()()()', 0),
    ('(((())))', 0),
    ('()()()()()()(', 1),
    ('((((())))', 1),
    (')))(((', -1),
    (')()()()()()', -1),
    ('no parens in this string', 'No parents')
]


@pytest.mark.parametrize('parens, result', PARAMS_TABLE)
def test_against_params(parens, result):
    """Test against the generated tests."""
    assert pp(parens) == result


def test_pp_type():
    """Raises type error"""
    with pytest.raises(TypeError):
        pp(1337)
