class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}

        for i, v in enumerate(nums):
            if target - v in hash_map:
                return hash_map[target-v], i
            else:
                hash_map[v] = i
        