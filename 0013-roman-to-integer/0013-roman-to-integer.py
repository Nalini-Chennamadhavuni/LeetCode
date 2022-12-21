class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
       
        romandict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        for i in range(len(s)):
            if i+1 < len(s) and romandict[s[i]] < romandict[s[i+1]] :
                n -= romandict[s[i]]
            else:
                n += romandict[s[i]]
        return n