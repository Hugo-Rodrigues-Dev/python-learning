"""Recursion and backtracking patterns with beginner-friendly examples.

Recursion helps solve a big problem by solving smaller versions of it, while
backtracking explores every valid option by undoing choices that do not work.
"""

from typing import List


def factorial(n: int) -> int:
    """Return n! using recursion with a clear base case."""
    if n < 0:
        raise ValueError("factorial is only defined for non-negative integers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using recursion with memoization."""
    memo = {0: 0, 1: 1}

    def helper(k: int) -> int:
        if k not in memo:
            memo[k] = helper(k - 1) + helper(k - 2)
        return memo[k]

    if n < 0:
        raise ValueError("fibonacci is only defined for non-negative integers")
    return helper(n)


def generate_subsets(nums: List[int]) -> List[List[int]]:
    """Generate the power set of nums using backtracking."""
    result: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        result.append(path.copy())
        for index in range(start, len(nums)):
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return result


def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    """Find combinations that add up to target; numbers can repeat."""
    result: List[List[int]] = []
    nums.sort()

    def backtrack(start: int, remaining: int, path: List[int]) -> None:
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0:
            return
        for index in range(start, len(nums)):
            choice = nums[index]
            path.append(choice)
            backtrack(index, remaining - choice, path)
            path.pop()

    backtrack(0, target, [])
    return result


# Demonstration
print("factorial(5) =", factorial(5))
print("fibonacci(8) =", fibonacci(8))
print("generate_subsets([1, 2, 3]) =", generate_subsets([1, 2, 3]))
print("combination_sum([2, 3, 6, 7], 7) =", combination_sum([2, 3, 6, 7], 7))
