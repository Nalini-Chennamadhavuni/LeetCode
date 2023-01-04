class Solution(object):

    def searchInsert(self, nums, target):
        if nums[-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0
        else:
            return self.search(0, len(nums)-1, nums, target)
    def search(self, start, end, nums, target):
        mid = start + (end - start)/2
        if start == end:
            return end 
        if nums[mid] < target:
            return self.search(mid+1, end, nums, target)
        elif nums[mid] > target:
            return self.search(start,mid,nums,target)
        else:
            return mid