#
# @lc app=leetcode id=3375 lang=python3
#
# [3375] Minimum Operations to Make Array Values Equal to K
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        replaced = set()

        for num in nums:
            if num < k:
                return -1

            if num != k and num not in replaced:
                replaced.add(num)
                count += 1
        return count
             
# @lc code=end

