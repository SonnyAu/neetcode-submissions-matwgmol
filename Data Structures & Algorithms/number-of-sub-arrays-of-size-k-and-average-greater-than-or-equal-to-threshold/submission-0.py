class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        window = []
        ans = 0
        curSum = 0
        for R in range(len(arr)):
            curSum += arr[R]
            if R >= k - 1:
                if curSum >= threshold:
                    ans += 1
                curSum -= arr[R - k + 1]
        return ans