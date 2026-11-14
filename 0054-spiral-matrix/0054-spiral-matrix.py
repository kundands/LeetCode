class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []


        ret = []
        l,t = 0, 0
        r,b = len(matrix[0]) - 1, len(matrix) - 1
        while l<=r and t <= b:
            for i in range(l, r+1):
                ret.append(matrix[t][i])
            t += 1

            for i in range(t, b+1):
                ret.append(matrix[i][r])
            r -= 1

            if t <= b:
                for i in range(r, l-1, -1):
                    ret.append(matrix[b][i])
                b -= 1
            
            if l <= r:
                for i in range(b, t-1, -1):
                    ret.append(matrix[i][l])
                l += 1
        
        return ret
                
