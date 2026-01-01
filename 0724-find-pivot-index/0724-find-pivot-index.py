class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = 0
        lsum = 0
        for i in range(len(nums)):
            totalsum += nums[i]

        for i in range(len(nums)):
            rsum = totalsum - lsum - nums[i]
            if rsum == lsum:
                return i
            lsum += nums[i]
        return -1