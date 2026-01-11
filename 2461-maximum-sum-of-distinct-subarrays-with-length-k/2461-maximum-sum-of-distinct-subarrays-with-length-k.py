class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set()
        cursum = maxsum = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in s or len(s) == k:
                s.remove(nums[l])
                cursum -= nums[l]
                l +=1
            cursum += nums[r] 
            s.add(nums[r])
            if len(s) == k:
                maxsum = max(cursum, maxsum)
            
        return maxsum