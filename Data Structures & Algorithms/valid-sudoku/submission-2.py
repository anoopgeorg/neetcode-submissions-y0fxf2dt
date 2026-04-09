from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        sub_grid = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                # Is the element unique in the row?
                if board[r][c] in rows[r]:
                    return False
                else:
                    rows[r].append(board[r][c])
                
                # Is the element unique in the column?
                if board[r][c] in cols[c]:
                    return False
                else:
                    cols[c].append(board[r][c])
                
                # Is the element unique in the sub grid?
                if board[r][c] in sub_grid[(r//3,c//3)]:
                    return False
                else:
                    sub_grid[r//3,c//3].append(board[r][c])

        return True