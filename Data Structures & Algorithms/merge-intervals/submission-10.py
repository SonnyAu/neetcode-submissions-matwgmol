class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        new = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new[-1][1]:
                maxV = max(intervals[i][1], new[-1][1])
                new[-1][1] = maxV
            else:
                new.append(intervals[i])
            
        return new
        