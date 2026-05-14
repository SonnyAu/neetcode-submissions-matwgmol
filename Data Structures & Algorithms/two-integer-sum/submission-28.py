from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        setup:
        use a hashmap to store value: index
        algo:
        if target - curr num in hashmap, return indices accordingly
        else add curr num: index to the hashmap
        '''

        seen = defaultdict(int)
        # 7 - 4 = 3
        # {3: 0 }
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i


        