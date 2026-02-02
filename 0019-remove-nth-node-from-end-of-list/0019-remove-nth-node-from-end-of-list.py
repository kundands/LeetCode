# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        new_n = ListNode(0, head)
        s = new_n
        f = new_n

        for i in range(n+1):
            f = f.next

        while f is not None:
            s = s.next
            f = f.next
        
        s.next = s.next.next

        return new_n.next
        