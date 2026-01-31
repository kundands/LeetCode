class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        nu_char = len(chars)
        if nu_char < 2:
            return nu_char

        i = j = 0 
        while i < nu_char:
            count = 1
            while i < nu_char -1 and chars[i] == chars[i+1]:
                count += 1
                i += 1

            chars[j] = chars[i]
            j += 1
            
            if count > 1:
                for val in str(count):
                    chars[j] = val
                    j += 1

            i += 1
        return j




        