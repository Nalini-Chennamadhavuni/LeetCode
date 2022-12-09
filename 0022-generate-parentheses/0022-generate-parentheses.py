class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        stack2 = []
       
        def backtrack(openP, closeP):
            if openP == closeP == n:
                stack2.append(''.join(stack))
            if openP < n:
                stack.append('(')
                backtrack(openP+1, closeP)
                stack.pop()
                
            if closeP < openP:
                stack.append(')')
                backtrack(openP, closeP+1)
                stack.pop()
                
                
        backtrack(0,0)
        return stack2