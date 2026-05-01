class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, ans = 0, 0
        maxQ = deque()
        minQ = deque()

        for r in range(len(nums)):
            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()
            maxQ.append(nums[r])
            while minQ and minQ[-1] > nums[r]:
                minQ.pop()
            minQ.append(nums[r])


            diff = maxQ[0] - minQ[0]
            while diff > limit:
                
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                if nums[l] == minQ[0]:
                    minQ.popleft()
                diff = abs(maxQ[0] - minQ[0])
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        

        