class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if not x or x[0] == '-':
            return False
        if len(x) == 1:
            return True
        else:
            a, b = 0, len(x) - 1
            while a < b:
                if x[a] == x[b]:
                    a += 1
                    b -= 1
                else:
                    return False
            return True