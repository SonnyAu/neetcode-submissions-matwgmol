class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            for s in strs:
                print(i)
                if s == '':
                    return ''
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
        