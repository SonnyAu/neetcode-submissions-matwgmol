class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        
        for i in range(len(nums)):
            totalSum = prefix[-1]
            leftSum = prefix[i - 1] if i > 0 else 0
            rightSum = totalSum - prefix[i]
            if leftSum == rightSum:
                return i
        return -1
        