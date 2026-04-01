class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copyArr = nums[:]
        for copyNum in copyArr:
            index = nums.index(copyNum)
            print(index)
            for i in range(index + 1, len(nums), 1):
                if nums[i] == copyNum:
                    print(nums[i])
                    print(copyNum)
                    return True
        return False

