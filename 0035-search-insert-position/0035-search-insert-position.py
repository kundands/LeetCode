class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        h = n -1
        lb = n
        while l <= h:
            m = (l + h)//2
            if nums[m] >= target:
                lb = m
                h = m - 1
            else:
                l = m + 1

        return lb
    
