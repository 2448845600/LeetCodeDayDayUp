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


if __name__ == '__main__':
    # 5个节点，无向图，连接关系如下，求有多少颗树
    trees = [[0, 1], [1, 2], [3, 4]]

    uf = UnionFind(5)  # 初始有5个节点
    for a, b in trees:
        uf.union(a, b)  # a,b是连通的

    print(uf.get_count())
