class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = {0:1}
        curSum = 0
        res = 0
        for n in nums:
            curSum += n
            needed = curSum - k
            res += prefix.get(needed, 0)
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return res
        