class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        print(dict(sorted(freq.items(), key=lambda item: -1 * item[1])))

        sortedFreq = (list(dict(sorted(freq.items(), key=lambda item: -1 * item[1]))))
        return (sortedFreq[:k])

        