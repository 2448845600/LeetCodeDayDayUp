class Solution:

    def numIslands(self, grid) -> int:
        def dfs(grid, i, j, m, n, used):
            used[i][j] = True

            steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dx, dy in steps:
                newx = i + dx
                newy = j + dy
                if 0 <= newx < m and 0 <= newy < n and not used[newx][newy] and grid[newx][newy] == "1":
                    dfs(grid, newx, newy, m, n, used)

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        count = 0
        used = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (not used[i][j]):
                    dfs(grid, i, j, m, n, used)
                    count += 1

        return count

    def numIslandsBFS(self, grid) -> int:
        from queue import Queue

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        count = 0
        used = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (not used[i][j]):
                    que = Queue()
                    que.put((i, j))
                    count += 1

                    while not que.empty():
                        cur_x, cur_y = que.get()
                        steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                        for dx, dy in steps:
                            new_x = cur_x + dx
                            new_y = cur_y + dy
                            if 0 <= new_x < m and 0 <= new_y < n and not used[new_x][new_y] \
                                    and grid[new_x][new_y] == "1":
                                que.put((new_x, new_y))
                                used[new_x][new_y] = True

        return count

    def numIslandsUF(self, grid) -> int:

        # UnionFind Set
        class UnionFind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root: return

                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1
                else:
                    self.parent[p_root] = q_root
                    self.rank[q_root] += 1

                self.count -= 1

        # main
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        # 实际节点编号从 0 ~ row*col-1，虚拟节点编号row * col
        dummy_node = row * col  # 多出来的一个节点，虚拟节点
        uf = UnionFind(dummy_node + 1)  # 多开一个空间，把水域 "0" 都归到这个虚拟节点
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                else:
                    for dx, dy in [[1, 0], [0, 1]]:
                        new_x = i + dx
                        new_y = j + dy
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))

        return uf.get_count() - 1  # 删除虚拟节点


if __name__ == '__main__':
    s = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(s.numIslandsBFS(grid))
