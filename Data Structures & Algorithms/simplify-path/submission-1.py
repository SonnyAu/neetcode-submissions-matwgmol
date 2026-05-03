class Solution:
    def simplifyPath(self, path: str) -> str:
        # ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        # ['', '..', '', '']
        # ['', '..', '', '_home', 'a', 'b', '..', '', '', '']



        
        parts = path.split("/")
        stack = []
        for c in parts:
            if c == '' or c == '.':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        if stack:
            stack.insert(0,"")
        else:
            stack.insert(0,"/")
        new_path = "/".join(stack)
        return new_path
        