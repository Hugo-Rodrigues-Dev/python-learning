"""Quick Sort: efficient divide-and-conquer sorting algorithm.

Idea (simple recursive version):
- Pick a pivot.
- Partition remaining items into < pivot, == pivot, > pivot.
- Recursively sort the smaller and larger parts, then concatenate.

Average: O(n log n) time, Worst: O(n^2) (bad pivot choices), Space: O(n).
"""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """Return a sorted copy of `arr` using a simple quicksort (not in-place)."""
    # Base case: lists of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr.copy()
    # Choose a pivot (here, the middle element)
    pivot = arr[len(arr) // 2]
    # Partition into three lists using list comprehensions
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort left and right, then concatenate
    return quick_sort(left) + mid + quick_sort(right)


# Demo
data = [9, 3, 7, 1, 8, 2, 5]
print("Original:", data)
print("Quick sorted:", quick_sort(data))   # returns a new sorted list
print("Original unchanged:", data)
