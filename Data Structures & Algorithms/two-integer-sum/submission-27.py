from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        define our hash table
        one-pass array loop
        
        algo:
        loop through array
        if target - curr num in hash table 
        then return indices
        else add curr num: index to hash table
        '''

        seen = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i

        