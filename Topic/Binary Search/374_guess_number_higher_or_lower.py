# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).

class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 1, n

        while l <= r:
            mid = (l + r)//2 
            pick = guess(mid)

            if pick == 0:
                return mid
            elif pick == -1:
                r = mid - 1
            else:
                l = mid + 1

        return l


