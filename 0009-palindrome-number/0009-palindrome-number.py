class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > -1: 
            return( True if (int(str(x)[::-1])) == x else False)
        else:
            return False 