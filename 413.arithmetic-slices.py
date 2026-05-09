from typing import List
def numberOfArithmeticSlices(nums: List[int]) -> int:
    sub_count = 0
    n = len(nums)
    if n < 3:
        return sub_count
    curr_diff = nums[1] - nums[0]
    curr_len = 2
    for i in range(2, n):
        diff = nums[i] - nums[i - 1]
        if curr_diff != diff:
            curr_len = 2
            curr_diff = diff
        else:
            curr_len += 1
        
        if curr_len >= 3:
            sub_count += (curr_len - 2)

    return sub_count

print(numberOfArithmeticSlices([1,2,3,4]))
