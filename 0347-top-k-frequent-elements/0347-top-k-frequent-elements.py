class Solution(object):
    def topKFrequent(self, nums, k):
        numsdict = {}
        count = 0
        for i in nums:
            #print("i is", i, "count is ", count, "dict has:", numsdict)
            if i in numsdict:
                count = numsdict[i] + 1
                numsdict[i] = count
            
            else:
                count = 1
                numsdict[i] = count
            
        return (sorted(numsdict, key=numsdict.get, reverse=True)[:k])
    