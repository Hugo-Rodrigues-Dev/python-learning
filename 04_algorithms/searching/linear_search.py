"""Linear Search: scan each element until the target is found.

Time: O(n) in worst case. Works on any list (no need to be sorted).
"""

from typing import List, Any, Optional


def linear_search(arr: List[Any], target: Any) -> Optional[int]:
    """Return the index of `target` in `arr`, or None if not found."""
    # Go through items one by one
    for idx, value in enumerate(arr):  # enumerate gives (index, value)
        # If we find the target, return its position
        if value == target:
            return idx
    # If we never found it, return None (not present)
    return None


# Demo (example usage)
data = ["a", "b", "c", "d"]
print("Data:", data)
print("Find 'c':", linear_search(data, "c"))  # returns 2
print("Find 'x':", linear_search(data, "x"))  # returns None
