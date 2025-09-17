"""Binary Search: search a sorted array by halving the range each step.

Requires the input to be sorted.
Time: O(log n), Space: O(1) (iterative) or O(log n) (recursive call stack).
"""

from typing import List, Optional


def binary_search_iterative(arr: List[int], target: int) -> Optional[int]:
    """Return the index of `target` using iterative binary search, else None"""
    # Search bounds (inclusive)
    left, right = 0, len(arr) - 1
    while left <= right:
        # Middle index of current range
        mid = (left + right) // 2
        # Compare target with middle element
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            # Target is on the right half
            left = mid + 1
        else:
            # Target is on the left half
            right = mid - 1
    # Not found
    return None


def binary_search_recursive(arr: List[int], target: int) -> Optional[int]:
    """Recursive wrapper that returns the index of `target` or None."""

    def helper(lo: int, hi: int) -> Optional[int]:
        # Base case: empty range -> not found
        if lo > hi:
            return None
        # Choose middle of current range
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            # Recurse into right half
            return helper(mid + 1, hi)
        else:
            # Recurse into left half
            return helper(lo, mid - 1)

    return helper(0, len(arr) - 1)


# Demo (remember: array must be sorted)
data = [1, 3, 5, 7, 9, 11]
print("Sorted data:", data)
print("Iterative find 7:", binary_search_iterative(data, 7))  # index 3
print("Iterative find 4:", binary_search_iterative(data, 4))  # None
print("Recursive find 9:", binary_search_recursive(data, 9))  # index 4
print("Recursive find 2:", binary_search_recursive(data, 2))  # None
