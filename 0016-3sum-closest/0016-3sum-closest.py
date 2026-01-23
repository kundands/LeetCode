class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h = i+1, n-1
            while l < h:
                cur_sum = nums[i] + nums[l] + nums[h]

                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return cur_sum
                
                elif cur_sum < target:
                    l += 1
                else:
                    h -= 1
                
        return closest_sum
