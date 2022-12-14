class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sdict = {}
        for a in range(len(s)):
            if s[a] in sdict:
                sdict[s[a]] = sdict[s[a]]  + 1
            else:
                sdict[s[a]] = 1
        
            #sdict.update({s[a]:1})
            
            if t[a] in sdict:
                sdict[t[a]] = sdict[t[a]] - 1
            else:
                sdict[t[a]] = - 1
        
        for v in sdict.values():
            if v != 0:
                return False
        return True        
    
    