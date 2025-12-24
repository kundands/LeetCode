# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        num = []

        while head:
            num.append(head.val)
            head = head.next

        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] == num[r]:
                l += 1
                r -= 1
            else:
                return False         
        return True   




