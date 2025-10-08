"""Two-pointer patterns for sorted arrays and string processing."""

from typing import List, Optional, Tuple


def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices (0-based) of two numbers that sum to target, if any."""
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1
    return None


def reverse_vowels(text: str) -> str:
    """Return text with vowels reversed, keeping other characters in place."""
    vowels = set("aeiouAEIOU")
    chars = list(text)
    left, right = 0, len(chars) - 1

    while left < right:
        if chars[left] not in vowels:
            left += 1
            continue
        if chars[right] not in vowels:
            right -= 1
            continue
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


# Demonstration
numbers = [1, 2, 3, 4, 6, 8, 11]
print("two_sum_sorted([1, 2, 3, 4, 6, 8, 11], 10) =", two_sum_sorted(numbers, 10))
print("two_sum_sorted([1, 2, 3, 4, 6, 8, 11], 19) =", two_sum_sorted(numbers, 19))
print("reverse_vowels('hello world') =", reverse_vowels("hello world"))
