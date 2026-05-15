"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        '''
        setup:
        number line with ranges
        + 1 at start, -1 at end
        keep track of when meetings are happening at the same time (equals num of rooms needed)
        define hash map w/ the start and ends (+1, -1 respectively)
        algo:
        make and add to hash table w/ starts and ends
        sort hash table to loop through
        define curr meetings happening
        update meetings needed
        return
        '''

        meetings = defaultdict(int)

        for m in intervals:
            meetings[m.start] += 1
            meetings[m.end] -= 1
        '''
        {0: 1, 5: 1, 10: -1, 15: 1, 20: -1, 40: -1,} 
        curr = 0
        needed = 2
        '''
        curr = 0
        needed = 0

        for m in sorted(meetings.keys()):
            curr += meetings[m]

            needed = max(curr, needed)

        return needed

        