class Solution:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:
        next_nodes = [[] for _ in range(n + 1)]

        for edge in edges:
            next_nodes[edge[0]].append(edge[1])
            next_nodes[edge[1]].append(edge[0])

        from queue import Queue
        que = Queue()
        que.put((1, 0, 1.0))  # id, time, prob
        travel = set([1])
        while not que.empty():
            id, ct, prob = que.get()

            new_next_nodes = []
            for next_node in next_nodes[id]:
                if next_node not in travel:
                    travel.add(next_node)
                    new_next_nodes.append(next_node)
            for next_node in new_next_nodes:
                next_node_prob = prob / len(new_next_nodes)
                if next_node == target:
                    if ct + 1 == t:
                        return next_node_prob
                    elif ct + 1 < t:
                        for nnode in next_nodes[target]:
                            if nnode not in travel:
                                return 0.0
                        return next_node_prob
                    else:
                        return 0.0
                if ct + 1 < t:
                    que.put((next_node, ct + 1, next_node_prob))

        return 0.0


if __name__ == '__main__':
    s = Solution()
    print(s.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4))

    print(s.frogPosition(n=3, edges=[[2, 1], [3, 2]], t=1, target=2))
