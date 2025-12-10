class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        MaxArea = 0
        while l < r:
            CurArea = min(height[l], height[r]) * (r-l)
            if MaxArea < CurArea:
                MaxArea = CurArea
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        return MaxArea