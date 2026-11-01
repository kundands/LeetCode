class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        loop_sum = 0
        result = 0
        for i in range(0, n+1):
            loop_sum += i
            if i < n:
                result += nums[i]
        return loop_sum - result
            

        