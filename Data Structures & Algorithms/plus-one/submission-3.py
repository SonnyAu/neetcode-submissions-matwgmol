class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        i, one = 0, 1
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        digits.reverse()
        return digits
