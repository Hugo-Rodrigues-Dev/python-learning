"""Merge Sort: stable O(n log n) divide-and-conquer sorting algorithm.

Idea:
- Split the list into halves until single elements remain.
- Merge sorted halves by repeatedly taking the smallest head element.

Time: O(n log n), Space: O(n) for the merged copies.
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    # Merge two sorted lists into one sorted list
    result = []
    i = j = 0  # pointers for left and right
    while i < len(left) and j < len(right):
        # Take the smaller head element and advance that pointer
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining items (only one of these will add elements)
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: List[int]) -> List[int]:
    """Return a sorted copy of `arr` using merge sort."""
    # Base case: a list of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr.copy()
    # Split into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge the sorted halves
    return merge(left, right)


# Demo
data = [5, 2, 9, 1, 5, 6]
print("Original:", data)
print("Merge sorted:", merge_sort(data))   # returns a new sorted list
print("Original unchanged:", data)
