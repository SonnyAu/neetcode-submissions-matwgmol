class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        else:
            result = ""
            for i in range(len(strs)):
                result += strs[i] + '`'
            return result[:-1]

    def decode(self, s: str) -> List[str]:
        if s == 'empty':
            return []
        return s.split("`")
