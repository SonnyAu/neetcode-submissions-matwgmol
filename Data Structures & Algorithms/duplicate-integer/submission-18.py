from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = defaultdict(int)

        for i in nums:
            if duplicates[i] > 0:
                return True
            duplicates[i] += 1
        return False
        