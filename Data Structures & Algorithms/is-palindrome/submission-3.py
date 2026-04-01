import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.replace(" ", "").lower()

        left = 0
        right = len(cleaned) - 1

        while left < right:

            while left < right and not cleaned[left].isalnum():
                left += 1
            while left < right and not cleaned[right].isalnum():
                right -= 1
            if cleaned[left] != cleaned[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        