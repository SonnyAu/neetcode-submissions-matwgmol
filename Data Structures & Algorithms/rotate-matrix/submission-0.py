class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bot = l, r


                topLeft = matrix[top][l + i]

                # bot-left -> top-left
                matrix[top][l + i] = matrix[bot - i][l]

                # bot-right -> bot-left
                matrix[bot - i][l] = matrix[bot][r - i]

                #top-right -> bot-right
                matrix[bot][r - i] = matrix[top + i][r]

                # top-left -> top-right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
            
        