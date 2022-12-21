class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        sdict = {')':'(','}' :'{', ']':'[' }
        
        for c in s:
            if c in sdict:
                if stack and stack[-1] == sdict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 
                
                                          