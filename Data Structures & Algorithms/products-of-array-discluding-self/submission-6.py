class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pref = [0] * n
        post = [0] * n

        pref[0] = post[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        for i in range(n):
            ans[i] = pref[i] * post[i]
        return ans