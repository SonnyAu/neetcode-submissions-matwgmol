class Solution:
    def simplifyPath(self, path: str) -> str:
        # ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        # ['', '..', '', '']
        # ['', '..', '', '_home', 'a', 'b', '..', '', '', '']



        
        parts = path.split("/")
        stack = []
        for c in parts:
            if c == '' or c == '.':
                print('1')
                continue
            elif c == '..':
                print('2')
                if stack:
                    stack.pop()
            else:
                print('3')
                stack.append(c)
        if stack:
            stack.insert(0,"")
        else:
            stack.insert(0,"/")
        new_path = "/".join(stack)
        return new_path
        