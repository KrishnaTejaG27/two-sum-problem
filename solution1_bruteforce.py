"""
Two Sum - Brute Force Approach

Idea:
Check every possible pair of numbers until we find
two numbers whose sum equals the target.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def two_sum(nums, target):

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# Example
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))

