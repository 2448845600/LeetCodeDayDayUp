class Solution:
    def numIslands2(self, m: int, n: int, positions):
        class UnionFind:
            def __init__(self, n):
                self.count = 0
                self.parent = [-1 for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def set_parent(self, i, p):
                self.parent[i] = p
                self.count += 1

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

        # main function
        grid = [[False for _ in range(n)] for _ in range(m)]
        uf = UnionFind(m * n)
        get_index = lambda x, y: x * n + y

        res = []
        for x, y in positions:
            if not grid[x][y]:
                grid[x][y] = True
                uf.set_parent(get_index(x, y), get_index(x, y))
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                        uf.union(get_index(x, y), get_index(nx, ny))
            res.append(uf.count)

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
    print(res)
    print(s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [1, 2]]))

    res = s.numIslands2(8, 2, [[7, 0]])
    print(res)
