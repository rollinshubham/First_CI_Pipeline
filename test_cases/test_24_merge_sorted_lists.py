
import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_basic_merge():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_empty_first_list():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_empty_second_list():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_both_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_duplicate_elements():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]


def test_negative_numbers():
    assert merge_sorted_lists([-5, -2, 1], [-4, 0, 3]) == [-5, -4, -2, 0, 1, 3]
