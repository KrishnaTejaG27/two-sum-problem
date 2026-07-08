"""
Two Sum - HashMap Approach

Idea:
Store each number and its index while iterating.

For every number:
    calculate the complement:
    complement = target - current number

If complement exists in the HashMap,
we found the answer.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


# Example
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
