from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            if freq[num]:
                freq[num] += 1
            else:
                freq[num] = 1

        arr = []
        for value, count in freq.items():
            arr.append([count, value])

        arr.sort()

        ans = []
        while len(ans) < k:
            ans.append(arr.pop()[1])
        return ans

        