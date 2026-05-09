class Solution(object):
    def twoSum(self, numbers, target):
        last_seen = {}
        for i, num in enumerate(numbers):
            if num not in last_seen:
                last_seen[target - num] = i
            else:
                return last_seen[num] + 1, i + 1

