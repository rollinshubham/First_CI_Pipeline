from program21 import largest_word


def test_normal_sentence():
    assert largest_word("Python programming is interesting") == "programming"


def test_single_word():
    assert largest_word("Hello") == "Hello"


def test_empty_sentence():
    assert largest_word("") == ""


def test_equal_length_words():
    assert largest_word("cat dog") == "cat"


def test_multiple_words():
    assert largest_word("I love computer science") == "computer"