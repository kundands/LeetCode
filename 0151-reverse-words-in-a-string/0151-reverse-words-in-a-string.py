class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = s.split()

        rev_words = words[::-1]
        return " ".join(rev_words)