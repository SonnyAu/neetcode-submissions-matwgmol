class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        else:
            res = ""
            
            for s in strs:
                res += s + "`"
            print(res[:-1])
            return res[:-1]

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        
        return s.split("`")
