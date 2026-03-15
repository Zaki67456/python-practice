import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Exercice import find_duplicates, difference_set, square_tuple, merge_dicts, ToDo, flatten_list_once


def test_find_duplicates():
    assert sorted(find_duplicates([1, 2, 2, 3, 4, 4, 5])) == [2, 4]
    assert find_duplicates([1, 2, 3]) == []
    assert sorted(find_duplicates([1, 1, 1])) == [1]


def test_difference_set():
    assert difference_set({1, 2, 3}, {2, 3, 4}) == {1}
    assert difference_set({1, 2}, {1, 2}) == set()
    assert difference_set({1, 2, 3}, set()) == {1, 2, 3}


def test_square_tuple():
    assert square_tuple((1, 2, 3)) == (1, 4, 9)
    assert square_tuple((0, 5)) == (0, 25)
    assert square_tuple(()) == ()


def test_merge_dicts():
    assert merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 5, 'c': 4}
    assert merge_dicts({}, {'a': 1}) == {'a': 1}
    assert merge_dicts({'a': 1}, {}) == {'a': 1}


def test_todo():
    todo = ToDo()
    todo.add_task("Buy milk")
    assert todo.list_tasks() == ["Buy milk"]
    todo.remove_task("Buy milk")
    assert todo.list_tasks() == []
    todo.remove_task("Non existent")  # should not raise


def test_flatten_list_once():
    assert flatten_list_once([[1, 2], [3, 4], 5]) == [1, 2, 3, 4, 5]
    assert flatten_list_once([1, 2, 3]) == [1, 2, 3]
    assert flatten_list_once([]) == []
