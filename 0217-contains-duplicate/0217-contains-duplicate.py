class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ahashmap = set()
        for n in nums:
            if n in ahashmap:
                return True
            ahashmap.add(n)