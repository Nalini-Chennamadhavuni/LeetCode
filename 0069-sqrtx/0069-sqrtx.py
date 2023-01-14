class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1:
            return x
        r = x
        l = 0

        while l <= r:
            m = (l + r) // 2  
            if (m * m) <= x <(m+1)*(m+1):
                return m
            elif x < (m * m):
               r = m
            else:
                l = m +1 