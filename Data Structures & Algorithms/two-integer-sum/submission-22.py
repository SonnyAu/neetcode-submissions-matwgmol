from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        positions = defaultdict(int)

        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in positions:
                return [positions[needed_num], i]
            else:
                positions[num] = i
        return 0
        
        