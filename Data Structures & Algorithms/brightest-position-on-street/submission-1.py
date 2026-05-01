from collections import defaultdict
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:

        diff = defaultdict(int)

        for i, a in lights:
            l, r = i - a, i + a
            diff[l] += 1
            diff[r + 1] = -1
        curr = max_bright = 0
        res = 0
        for k in sorted(diff):
            curr += diff[k]
            if curr > max_bright:
                max_bright = curr
                res = k
        return res
                



        