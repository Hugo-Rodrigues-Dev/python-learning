"""Bubble Sort: simple, stable O(n^2) sorting algorithm.

Idea:
- Repeatedly step through the list, compare adjacent items and swap if needed.
- After each pass, the largest remaining element "bubbles" to the end.

Pros: easy to understand; stable.
Cons: very slow for large lists (O(n^2) time), in-place O(1) space.
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Return a sorted copy of `arr` using bubble sort."""
    # Work on a copy so the original list isn't changed
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False  # track if any swaps happen in this pass
        # After each pass, the last i elements are in correct position
        for j in range(0, n - 1 - i):
            # Compare adjacent elements and swap if out of order
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        # Optimization: if no swaps happened, the list is already sorted
        if not swapped:
            break
    return a


# Demo (example usage)
data = [5, 1, 4, 2, 8]
print("Original:", data)
print("Bubble sorted:", bubble_sort(data))  # returns new sorted list
print("Original unchanged:", data)          # original list stays the same
