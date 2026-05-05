from collections import defaultdict
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        ranges = defaultdict(int)

        for i, r in lights:
            left = i - r
            right = i + r
            ranges[left] += 1
            ranges[right + 1] -= 1

        ans = 0
        curr = max_bright = 0

        for k in sorted(ranges):
            curr += ranges[k]
            if curr > max_bright:
                max_bright = curr
                ans = k
        return ans
            


        