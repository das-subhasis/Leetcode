#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        counter = 1

        for num in nums[1:]:
            if num == candidate:
                counter += 1
            else:
                if counter == 0:
                    candidate = num
                    counter = 1
                    continue
                counter -= 1
        return candidate
                
# @lc code=end

