def formatted_print_board(board:list[list[int]]):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f"{board[i][j]}", end=' ' if j != len(board[i]) - 1 else '\n')

from collections import deque

class Solution:
    def knightChessboard(self, board_size:int, start:tuple[int], end:tuple[int]) -> int:
        orient = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]] #Knights can move about the board in an L-shape
        visit = set()
        board = [[0 for j in range(board_size)] for i in range(board_size)]
        board[start[0]][start[1]] = 1
        board[end[0]][end[1]] = 1
        rows, cols = len(board), len(board[0])
        moves = 0

        def bfs(row:int, col:int):
            q = deque()
            visit.add((row, col))
            q.append((row, col))
            print(q)
            while q: #while q is not empty
                row, col = q.popleft()
                print(orient)
                for dr, dc in orient:
                    r,c = row + dr, col + dc
                    print(r, c)
                    if r in range(rows) and c in range(cols):
                        if board[r][c] == "1" and (r,c) not in visit:
                            q.append((r,c))
                            visit.add((r,c))
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "1" and (r,c) not in visit:
                    print("2", r,c)
                    bfs(r,c)
                    moves += 1

        # formatted_print_board(board)
        return moves

sol = Solution()
ret = sol.knightChessboard(5, (0,1), (4, 4))
print("RET:", ret)
assert ret == 3