'''
转换到上下左右

注意！！！
python 默认迭代999层就自动终止，需要设定迭代深度

import sys
sys.setrecursionlimit(100000)
'''


class Solution:
    def hasValidPath(self, grid) -> bool:
        import sys
        sys.setrecursionlimit(100000)

        step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dir = [[], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1]]

        m, n = len(grid), len(grid[0])
        used = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y, used):
            used[x][y] = True

            if x == m - 1 and y == n - 1:
                return True

            id = grid[x][y]
            a, b, c, d = False, False, False, False
            for i in range(len(step)):
                dx, dy = step[i]
                nx = x + dx
                ny = y + dy
                if dir[id][i] and 0 <= nx < m and 0 <= ny < n and not used[nx][ny]:
                    if i == 0 and grid[nx][ny] in [2, 3, 4]:
                        a = dfs(nx, ny, used)
                    elif i == 1 and grid[nx][ny] in [2, 5, 6]:
                        b = dfs(nx, ny, used)
                    elif i == 2 and grid[nx][ny] in [1, 4, 6]:
                        c = dfs(nx, ny, used)
                    elif i == 3 and grid[nx][ny] in [1, 3, 5]:
                        d = dfs(nx, ny, used)

            return a or b or c or d

        return dfs(0, 0, used)
