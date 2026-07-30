class Solution:
	def maxAreaOfIsland(self, grid: list[list[int]]):
		ROWS, COLS = len(grid), len(grid[0])
		visit = set()
		def dfs(r, c):
			if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
				return 0
			visit.add ((r, c))
			return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs (r, c + 1) + dfs(r, c - 1))
		area = 0
		for r in range (ROWS) :
			for c in range (COLS):
				area = max(area, dfs(r, c))
		return area

def test_testcase(grid:list[list[int]], expected:int, test_numb:int):
    sol = Solution()
    ret = sol.maxAreaOfIsland(grid)
    print(f"Test Case {test_numb}:")
    print("\tReturned:", ret)
    assert ret == expected
    print("\tExpected:", expected)

test_case_1_grid = [[0,1,0,0,0],
					[1,1,1,0,0],
                    [0,0,0,0,1],
                    [1,1,0,1,1]]
test_case_1_exp = 4
test_testcase(test_case_1_grid,
			  test_case_1_exp,
              1)

test_case_2_grid = [[1, 1, 0, 0, 0],
					[1, 1, 1, 0, 0],
					[1, 0, 0, 0, 0],
					[0, 0, 1, 1, 1],
					[0, 1, 1, 1, 1]]
test_case_2_exp = 7
test_testcase(test_case_2_grid,
			  test_case_2_exp,
			  2)