class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        for r in range(1, n):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l +=1
        return l+1

        