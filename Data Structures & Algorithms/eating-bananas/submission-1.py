class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        
        while L <= R:
            mid = L + (R - L) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            if hours > h:
                L = mid + 1
            else:
                R = mid - 1
        return L

        