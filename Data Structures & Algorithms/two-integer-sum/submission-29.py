from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = defaultdict(int)

        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[curr] = i
        