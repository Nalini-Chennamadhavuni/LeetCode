class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        if len(x) == 1:
            return True
        begin = 0
        end = len(x) - 1
        while begin < end:
            if x[begin] == x[end]:
                begin += 1
                end -= 1
            else:
                return False
        return True
                