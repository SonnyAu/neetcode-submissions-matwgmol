class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:


        l = count = 0
        ans = 999
        for r in range(len(blocks)):
            c = blocks[r]

            if c == 'W':
                count += 1
            print(blocks[l:r])
            while (r - l + 1) > k:
                if blocks[l] == 'W':
                    count -= 1
                l += 1
            if (r - l + 1) == k:
                ans = min(ans, count)
           
        return ans
        