class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:


        '''
        algo:
        first pass is to go through r's and c's to swap accordingly (start from end of row)
        second pass is to rotate, start with going through c's then reversed r's (append to temp row to append to ans)
        return ans

        '''

        rows, cols = len(boxGrid), len(boxGrid[0])
        # [".",".","#","#","#","#"], i = 4
        #           | 
        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if boxGrid[r][c] == '#':
                    boxGrid[r][i], boxGrid[r][c] = boxGrid[r][c], boxGrid[r][i]
                    i -= 1
                elif boxGrid[r][c] == '*':
                    i = c - 1

        ans = []
        '''
        ["#","#","*",".","*","."],
        ["#","#","#","*",".","."],
        [".","#","#",".","#","."]
        row = ['.', '#', '#']
        '''

        for c in range(cols):
            row = []
            for r in reversed(range(rows)):
                row.append(boxGrid[r][c])
            ans.append(row)
        return ans

        
        