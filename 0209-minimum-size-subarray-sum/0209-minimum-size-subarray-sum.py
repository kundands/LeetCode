class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minlen = float('inf')
        l = 0
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum >= target:
                minlen = min(minlen, r-l+1)
                cursum -= nums[l]
                l += 1
                
        return minlen if minlen != float('inf') else 0   