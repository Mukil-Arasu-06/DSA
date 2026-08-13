# LeetCode: Contains Duplicate

## Problem

Given an integer array `nums`, return `True` if any value appears at least twice. Otherwise, return `False`.

### Example

```python
nums = [1, 2, 3, 1]


| Iteration | `num` | `seen` before | `num in seen` | Action        | `seen` after |
| --------: | ----: | ------------- | ------------- | ------------- | ------------ |
|         1 |     1 | `{}`          | No            | Add `1`       | `{1}`        |
|         2 |     2 | `{1}`         | No            | Add `2`       | `{1, 2}`     |
|         3 |     3 | `{1, 2}`      | No            | Add `3`       | `{1, 2, 3}`  |
|         4 |     1 | `{1, 2, 3}`   | **Yes**       | Return `True` | `{1, 2, 3}`  |


How It Works
Create an empty set called seen.
Iterate through every number in nums.
Check whether the number is already inside seen.
If it is already there, return True.
Otherwise, add the number to seen.
If the loop finishes, return False.
Complexity
Type	Complexity
Time	O(n)
Space	O(n)
DSA Pattern

Array → Detect Duplicate → Hash Set → Iterate Once