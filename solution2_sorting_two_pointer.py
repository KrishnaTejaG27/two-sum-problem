"""
Two Sum - Sorting + Two Pointer Approach

Idea:
1. Store numbers with their original indexes.
2. Sort the numbers.
3. Use two pointers:
   - Left pointer starts at beginning.
   - Right pointer starts at end.
4. Move pointers based on the current sum.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


def two_sum(nums, target):

    nums_with_index = []

    for i, num in enumerate(nums):
        nums_with_index.append((num, i))

    nums_with_index.sort()


    left = 0
    right = len(nums_with_index) - 1


    while left < right:

        current_sum = (
            nums_with_index[left][0] +
            nums_with_index[right][0]
        )

        if current_sum == target:
            return [
                nums_with_index[left][1],
                nums_with_index[right][1]
            ]

        elif current_sum < target:
            left += 1

        else:
            right -= 1


    return []


# Example
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
