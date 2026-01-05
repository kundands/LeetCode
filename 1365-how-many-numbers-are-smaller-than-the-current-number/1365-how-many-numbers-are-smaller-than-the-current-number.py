class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        d = {}
        ret = []
        for i, v in enumerate(temp):
            if v not in d:
                d[v] = i
            
        for i in nums:
            ret.append(d[i])
        return ret

        