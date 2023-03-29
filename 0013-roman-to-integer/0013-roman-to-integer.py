class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romandict= {"I":1, "V": 5, "X":10, "L":50, "C":100 , "D":500, "M":1000}
        subtractdict= {"I" : ['V', 'X'], "X" : ['L', 'C'], "C" : ['D', 'M']  }
        total = 0
        end = len(s) - 1
        while end >= 0:
            if s[end-1] in subtractdict and s[end] in subtractdict[s[end-1]] and end != 0:
                    print("s[end] is ", s[end])
                    print("s[end -1] is ", s[end -1])
                    total += (romandict[s[end]] - romandict[s[end-1]])
                    end -= 2
            else:
                total += romandict[s[end]]
                end -= 1
        return total
                
                
                
            
                    