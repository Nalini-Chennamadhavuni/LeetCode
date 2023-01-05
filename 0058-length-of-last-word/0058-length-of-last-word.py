class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        isDone = False
        for c in s[::-1]:
            if c == ' ' and isDone:
                break
            if c != ' ':
                count += 1
                isDone = True
        return count