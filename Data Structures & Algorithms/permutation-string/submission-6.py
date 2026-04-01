from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''
        s1 is the main counter
        s2 is what is being checked
        if counter for s1's char > 1 then return false
        '''
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        
        if len(s1) > len(s2):
            return False
        for c in s1:
            freq1[c] += 1
        l = 0
        for r in range(len(s2)):
            while (r - l + 1) > len(s1):
                if s2[l] in freq2:
                    freq2[s2[l]] -= 1
                    if freq2[s2[l]] == 0:
                        del freq2[s2[l]]
                l += 1
            if s2[r] in s1:
                freq2[s2[r]] += 1
            if freq1 == freq2:
                return True
            

        return False