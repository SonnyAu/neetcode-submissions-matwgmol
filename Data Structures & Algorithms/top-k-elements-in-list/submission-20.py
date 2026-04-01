from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1

        arr = []
        for value, count in freq.items():
            arr.append([count, value])
        
        arr.sort()
        sol = []
        while len(sol) < k:
            sol.append(arr.pop()[1])


        return sol