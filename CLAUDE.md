# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Code

```bash
python L.py
```

To run with the interactive Python shell for testing individual functions:

```bash
python -c "from L import find_duplicates; print(find_duplicates([1,2,2,3,4,4,5]))"
```

To run doctests:

```bash
python -m doctest L.py -v
```

## Project Overview

This is a Python practice file (`L.py`) containing 6 exercises covering core Python data structures and OOP. Each exercise has a docstring describing the task with an example.

## Exercise Status

| # | Function/Class | Topic | Status |
|---|---|---|---|
| 1 | `find_duplicates(lst)` | Lists | Complete |
| 2 | `difference_set(a, b)` | Sets | Complete |
| 3 | `square_tuple(tpl)` | Tuples | **Buggy** — appends to a list but returns original `tpl` instead of a tuple of squared values |
| 4 | `merge_dicts(d1, d2)` | Dictionaries | Complete |
| 5 | `ToDo` class | OOP | Partial — `add_task` works; `remove_task` and `list_tasks` have `______YOUR_CODE_HERE_________` placeholders |
| 6 | `flatten_list_once(lst)` | Functions/Lists | **Not started** — placeholder only |
