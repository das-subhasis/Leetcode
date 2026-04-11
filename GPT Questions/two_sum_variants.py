#  Given an array, return True if any two numbers add up to the target, else False.
#  nums = [5, 1, 7, 2], target = 8 → True

from typing import List
from collections import Counter


def two_sum(nums: List, target: int):
    visited = {}
    for index, num in enumerate(nums):
        seen = target - num
        if seen in visited:
            return True
        else:
            visited[num] = index
    return False

# Check if array has duplicates
# Return True if any number appears twice.


def check_duplicates(nums: List):
    freq_map = Counter(nums)
    duplicates = []
    for num, freq in freq_map.items():
        if freq >= 2:
            duplicates.append(num)
    return duplicates

# First pair of numbers with difference k
# Given array and k, find first pair where abs(a - b) = k.
# nums = [4, 1, 7, 10], k = 3 → pair (4, 1) or (7, 10)
def find_diff_k_pairs(nums: List, k: int):
    visited = {}
    for index, num in enumerate(nums):
        seen_1 = abs(num + k)
        seen_2 = abs(num - k)
        if seen_1 in visited:
            return [index, visited[seen_1]]
        if seen_2 in visited:
            return [index, visited[seen_2]]
        visited[num] = index
    return None

# Subarray Sum “0” Check
# Return True if a subarray sums to 0.
# I have not understood this

# Two Sum on a Stream
# keep track of the elements incoming with their index on hasmap
# perform the same two sum op on find(target)
    