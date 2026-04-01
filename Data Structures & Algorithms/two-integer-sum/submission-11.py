from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = defaultdict(int)

        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index
        return
        