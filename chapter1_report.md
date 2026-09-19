# Report — `chapter1.py`

**File:** `E:\Life\started\chapter1.py`
**Type:** Python learning scratchpad / practice notes
**Report generated:** 2026-09-19
**Size:** ~784 lines (the large majority are commented-out practice snippets)

---

## 1. Overview

`chapter1.py` is a personal practice file used to re-learn Python fundamentals. It's structured as a running notebook: each concept is tried out in a small snippet, then commented out before moving to the next. It covers a genuinely broad sweep — from basic types and string formatting all the way up to decorators, generators, context managers, and custom exceptions.

Only a handful of lines are **active** (uncommented). Everything else is preserved as reference notes.

---

## 2. Topics covered

Grouped by theme, in roughly the order they appear:

### Fundamentals
- **ASCII / `ord()`** — looping over the alphabet and printing character codes
- **Finding the largest number** in a list with a running `largest` variable
- **Types & `isinstance()`** — checking `str` / `float` / `int`
- **`%`-style string formatting** — `%s`, `%d`, `%f`, and formatting with tuples
- **Strings** — `len()`, slicing with a step (`astring[0:9:2]`), quotes

### Control flow
- **Booleans & identity** — `is` vs `==`, `id()`, `not`
- **Truthiness** — empty vs non-empty lists, zero vs non-zero in `if`
- **Loops** — `for`, `range(start, stop, step)`, `while`
- **`print()` options** — `sep=` and `end=`

### Functions
- Defining functions, `return`, `sum_two_numbers(a, b)`
- Returning and processing lists (`list_benefits` / `build_sentence`)
- **`*args` / `**kwargs`** — variadic and keyword arguments
- **Type hints** — `def surface_area_of_cube(data: float) -> int`

### Data structures
- **Lists** — indexing (incl. negative), slicing, membership (`in`), slice-assignment, `append()`, `extend()` (with lists and tuples), `pop()`
- **List comprehensions** — filtering (`[x for x in fruits if 'r' in x]`), `range`-based
- **Bubble sort** — nested loops with tuple-swap
- **Tuple unpacking / swapping** — `a, b = b, a`
- **Dictionaries** — creating, `del`, `pop()`, `.items()`, `.keys()`, `.values()`, membership tests
- **`copy` module** — `copy.copy()` (shallow) vs `copy.deepcopy()` (deep), and identity checks with `id()` / `is`

### Object-oriented programming
- **Procedural vs OOP** — comparison notes
- **Classes** — `self`, class variables vs local variables inside methods
- **`__init__`** constructors (`Car`)
- **`@dataclass`** — `User` and `Vehicle` examples

### Advanced / idiomatic Python
- **Modules** — `import draw`, and the `if __name__ == '__main__':` guard
- **Decorators** — a `timeit` timer (using `functools.wraps`) and a `retry` decorator
- **Context managers** — `__enter__` / `__exit__` and the `with` statement
- **Generators** — `yield`, generator vs normal function, `next()`, a `paginate()` helper
- **Custom exceptions** — `InsufficientFundsError`, `raise`, `try/except`
- **Rate-limiting** context manager combining a custom exception with `with`
- **HTTP requests** — `requests.get()` with `ConnectionError` handling

---

## 3. Currently active (uncommented) code

Most of the file is commented out. These are the lines that actually run:

| Line(s) | Code | Notes |
|--------|------|-------|
| 14 | `import pdb` | Imported but never used |
| 15 | `from logging import raiseExceptions` | Imported but never used (see below) |
| 34–35 | `def get_user(): return "I'm"` | Defined but never called |
| 472–474 | `original = [...]; new_list = original.copy()` | Runs, but nothing is printed |
| 481, 528 | `import copy` | Imported twice (redundant) |
| 779 | `import requests` | |
| 781–784 | `requests.get("http://example.com")` in a `try/except` | **This is the only line with a real side effect** — running the file makes a live network call |

---

## 4. Observations & small fixes

These are minor — this is practice code, not production — but worth noting:

1. **Line 3 — typo in the alphabet.** The string `"ABCDEFGHIJKLMNOPQRSTUVXYZ"` is missing the letter **W** (it jumps `U, V, X`). Worth fixing if that snippet is ever re-run.

2. **Line 15 — `from logging import raiseExceptions`.** `raiseExceptions` is an internal flag in the `logging` module, not something you'd normally import. This looks like an accidental IDE autocomplete. It's unused and can be deleted.

3. **Unused imports.** `pdb` (line 14) and one of the duplicate `import copy` statements are never used. `import copy` appears on lines 481 and 528 — one is enough, and imports conventionally go at the top of the file.

4. **The `requests` call at the bottom runs on every execution.** Because it isn't commented out or guarded, opening/running the file always hits `example.com`. If you don't want that, wrap it in a function or an `if __name__ == '__main__':` block, or comment it out like the rest.

5. **General tidy-up idea.** Since this is a study log, you might eventually split topics into separate files (e.g. `strings.py`, `dicts.py`, `decorators.py`) or convert it into a Jupyter notebook — both make it much easier to re-run a single concept without scrolling past hundreds of commented lines.

---

## 5. Summary

`chapter1.py` is a solid, wide-ranging review of Python — you've touched nearly every core concept a working Python developer uses daily, including several intermediate topics (decorators, generators, context managers, dataclasses, custom exceptions). The main cleanup items are trivial: remove the unused imports, fix the alphabet typo, and decide whether the `requests` call at the end should really run on every execution.

**Concept coverage: broad. Cleanup needed: minimal.**
