# Two Sum Problem

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

---

## Example

### Input
nums = [2,7,11,15]
target = 9
#output
[0,1]
#Explanation
The numbers at the inde 0 and index 1 are:
2 + 7 = 9
Therefore, the answer is:
[0,1]

---

# Approaches

## 1. Brute Force Approach

### Idea

Check every possible pair of numbers until the target sum is found.

### Algorithm

1. Select the first number.
2. Compare it with every remaining number.
3. Return indices when the sum equals the target.

### Complexity

Time Complexity:

---

# Approaches

## 1. Brute Force Approach

### Idea

Check every possible pair of numbers until the target sum is found.

### Algorithm

1. Select the first number.
2. Compare it with every remaining number.
3. Return indices when the sum equals the target.

### Complexity

Time Complexity:
O(n2)

Space Complexity:
O(1)

---

## 2. Sorting + Two Pointer Approach

### Idea

Store numbers with their original indices, sort them, and use two pointers to find the target sum.

### Algorithm

1. Store values with indices.
2. Sort the values.
3. Use left and right pointers.
4. Move pointers based on the current sum.

### Complexity

Time Complexity:
O(nlogn)

Space Complexity:
O(n)

---

## 3. HashMap Approach (Optimal)

### Idea

Store previously visited numbers in a HashMap.

For each number:
complement = target - current number

If the complement already exists, we found the solution.

### Complexity

Time Complexity:
O(n)
Space Complexity:
O(n)

---

# Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Sorting + Two Pointer | O(n log n) | O(n) |
| HashMap | O(n) | O(n) |

---

# Key Learning

The Two Sum problem demonstrates how choosing the right data structure can improve performance.

The solution evolves from:
---

# Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Sorting + Two Pointer | O(n log n) | O(n) |
| HashMap | O(n) | O(n) |

---

# Key Learning

The Two Sum problem demonstrates how choosing the right data structure can improve performance.

The solution evolves from:
O(n²)
↓
O(n log n)
↓
O(n)
by reducing unnecessary searching optimization


