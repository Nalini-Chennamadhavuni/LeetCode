class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romandict= {"I":1, "V": 5, "X":10, "L":50, "C":100 , "D":500, "M":1000}
        total = 0
        for i in range(len(s)-1):
            if romandict[s[i]] < romandict[s[i + 1]]:
                total -= romandict[s[i]] 
            else:
                total += romandict[s[i]] 
        return total + romandict[s[-1]]
            
                    