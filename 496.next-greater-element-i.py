#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = nums2[::-1]
        stk = []
        count = {}
        for num in nums2:
            while stk and num > stk[-1]:
                count[stk.pop()] = num
            stk.append(num)
        while stk:
            count[stk.pop()] = -1
        return [count[num] for num in nums1]
# @lc code=end

