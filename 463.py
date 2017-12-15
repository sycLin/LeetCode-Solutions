class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        n_rows = len(grid)
        n_cols = len(grid[0])
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    # check neighboring zero's
                    if c == 0 or grid[r][c-1] == 0: # left
                        total += 1
                    if c == n_cols - 1 or grid[r][c+1] == 0: # right
                        total += 1
                    if r == 0 or grid[r-1][c] == 0: # up
                        total += 1
                    if r == n_rows - 1 or grid[r+1][c] == 0: # down
                        total += 1
        return total
        