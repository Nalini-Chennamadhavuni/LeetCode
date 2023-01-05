class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.strip()
        print(s)
        for i in s[::-1]:
            if i != ' ':
                count += 1
            else:
                break
        return count