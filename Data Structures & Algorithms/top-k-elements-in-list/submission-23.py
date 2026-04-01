from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        top_k = []
        for i, (num, count) in enumerate(freq.items()):
            top_k.append([count, num])

        top_k = sorted(top_k, reverse=True)
        ans = []

        while len(ans) < k:
            top = top_k.pop(0)[1]
            ans.append(top)

        return ans




        