class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        n_rows, n_cols = len(grid), len(grid[0])
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    area = 1
                    grid[r][c] = 0
                    queue = [(r, c)]
                    while len(queue) > 0:
                        # (1) dequeue
                        # (2) add to area and set to 0
                        # (3) enqueue neighbors if necessary
                        _r, _c = queue.pop(0)
                        if _r + 1 < n_rows and grid[_r+1][_c] == 1:
                            queue.append((_r+1, _c))
                            grid[_r+1][_c] = 0
                            area += 1
                        if _r -1 >= 0 and grid[_r-1][_c] == 1:
                            queue.append((_r-1, _c))
                            grid[_r-1][_c] = 0
                            area += 1
                        if _c + 1 < n_cols and grid[_r][_c+1] == 1:
                            queue.append((_r, _c+1))
                            grid[_r][_c+1] = 0
                            area += 1
                        if _c - 1 >= 0 and grid[_r][_c-1] == 1:
                            queue.append((_r, _c-1))
                            grid[_r][_c-1] = 0
                            area += 1
                    ret = max(ret, area)
        return ret
                        
        