class Solution(object):
    def SqSum(self, num):
        sum = 0
        while num > 0:
            no = num % 10
            sum += no**2
            num = num//10
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.SqSum(n)
        fast = self.SqSum(self.SqSum(n))
        while slow != fast:
            slow = self.SqSum(slow)
            fast = self.SqSum(self.SqSum(fast))
            # if slow == 1 or fast == 1:
            #     return True
        return slow == 1
    