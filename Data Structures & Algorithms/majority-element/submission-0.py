from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter()
        for n in nums:
            count[n] += 1
        return count.most_common(1)[0][0]

        