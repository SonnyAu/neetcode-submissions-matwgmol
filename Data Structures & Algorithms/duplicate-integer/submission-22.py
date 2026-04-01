from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        values = defaultdict(int)

        for num in nums:
            if num in values:
                return True
            else:
                values[num] += 1

        return False

        