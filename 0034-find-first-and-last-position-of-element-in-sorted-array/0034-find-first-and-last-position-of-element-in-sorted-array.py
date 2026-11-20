class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """     
        def lowerb(nums, target):
            lb = -1
            l = 0
            h = len(nums) - 1

            while l <= h:
                mid = (l + h) // 2
                if nums[mid] >= target:
                    lb = mid
                    h = mid - 1
                else:
                    l = mid + 1

            return lb

        def upperb(nums, target):
            n = len(nums)
            ub = n
            l = 0
            h = n - 1

            while l <= h:
                mid = (l + h) // 2
                if nums[mid] > target:
                    ub = mid
                    h = mid - 1
                else:
                    l = mid + 1

            return ub

        lb = lowerb(nums, target)

        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub = upperb(nums, target)

        return [lb, ub - 1]