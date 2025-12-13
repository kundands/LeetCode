class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s) -1
        l = 0 
        r = n
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # try skipping left character
                i, j = l + 1, r
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                if i >= j:
                    return True

                # try skipping right character
                i, j = l, r - 1
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                return i >= j   # True if palindrome, else False

        return True