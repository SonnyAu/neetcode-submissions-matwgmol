from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        arr = []
        for key, count in freq.items():
            arr.append([count, key])

        arr.sort()
        solution = []
        while len(solution) < k:
            solution.append(arr.pop()[1])
        return solution
