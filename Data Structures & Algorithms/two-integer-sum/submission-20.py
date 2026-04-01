from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffs = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs:
                return [diffs[diff], i]
            diffs[num] = i

        return [0, 0]


        