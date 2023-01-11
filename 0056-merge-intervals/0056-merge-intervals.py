class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        if len(intervals) == 1:
            return intervals
       
        merged = [intervals[0]]
       
        for i in range(1,len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return (merged)