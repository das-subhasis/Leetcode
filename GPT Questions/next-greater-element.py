class Solution:

    def nextGreaterElement(self, arr: list):
        result = [-1] * len(arr)
        stk = []
        for i in range(len(arr)):
            while stk and arr[i] > arr[stk[-1]]:
                top = stk.pop()
                result[top] = i - top
            stk.append(i)
        return result

solution = Solution()
print(solution.nextGreaterElement([5, 3, 7]))
