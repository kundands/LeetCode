class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
        return i+1