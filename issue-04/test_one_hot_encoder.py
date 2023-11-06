import pytest
from one_hot_encoder import fit_transform


def test_raises_error():
    """
    Test for fit_transform function
    with invalid input.
    """
    with pytest.raises(TypeError):
        fit_transform(1)


def test_one_string():
    """
    Test for fit_transform function
    with input consisting of a single string.
    """
    assert fit_transform('Squidward') == [('Squidward', [1])]


def test_multiple_string():
    """
    Test for fit_transform function
    with input consisting of different strings.
    """
    assert fit_transform('God', 'save', 'the', 'Queen') \
           == [('God', [0, 0, 0, 1]),
               ('save', [0, 0, 1, 0]),
               ('the', [0, 1, 0, 0]),
               ('Queen', [1, 0, 0, 0])]


def test_one_word_string():
    """
    Test for fit_transform function
    with input consisting of duplicate strings.
    """
    assert fit_transform('aa', 'aa', 'aa', 'aa') \
           == [('aa', [1]),
               ('aa', [1]),
               ('aa', [1]),
               ('aa', [1])]
