class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ch = "".join(ch.lower() for ch in s if ch.isalnum())
        s = ch
        if ch == s[::-1]:
            return True
        return False