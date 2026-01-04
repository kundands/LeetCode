class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        sec = 0 
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            sec += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2
        return sec
        