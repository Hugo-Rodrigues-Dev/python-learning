"""Sliding window techniques for fixed-size and elastic problems."""

from collections import Counter
from typing import Iterable, List


def max_sum_subarray(nums: Iterable[int], k: int) -> int:
    """Return the maximum sum of any contiguous subarray of length k."""
    nums_list = list(nums)
    if k <= 0 or k > len(nums_list):
        raise ValueError("k must be between 1 and the length of the list")

    window_sum = sum(nums_list[:k])
    best = window_sum
    for right in range(k, len(nums_list)):
        window_sum += nums_list[right] - nums_list[right - k]
        best = max(best, window_sum)
    return best


def longest_unique_substring(text: str) -> str:
    """Return the longest substring with all unique characters."""
    counts: Counter[str] = Counter()
    left = 0
    best_window = (0, 0)

    for right, char in enumerate(text):
        counts[char] += 1

        while counts[char] > 1:
            counts[text[left]] -= 1
            left += 1

        if right - left > best_window[1] - best_window[0]:
            best_window = (left, right)

    start, end = best_window
    return text[start : end + 1]


# Demonstration
print("max_sum_subarray([2, 1, 5, 1, 3, 2], 3) =", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
print("longest_unique_substring('abracadabra') =", longest_unique_substring("abracadabra"))
