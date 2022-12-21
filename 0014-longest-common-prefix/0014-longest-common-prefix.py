class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        newstr = ""
        for i in range(len(strs[0])):
            for c in strs:
                if i == len(c) or c[i]!= strs[0][i]:
                    return newstr
            newstr += strs[0][i]
                    
        return newstr
            