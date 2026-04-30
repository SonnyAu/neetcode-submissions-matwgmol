class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(l, r):
            while l <= r:
                mid = r - (r - l) // 2
                print(l, r)
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = r - (r - l) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
                

        