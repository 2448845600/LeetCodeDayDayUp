class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_num = [0 for _ in range(n)]
        for i in range(n):
            if leftChild[i] != -1:
                in_num[leftChild[i]] += 1
            if rightChild[i] != -1:
                in_num[rightChild[i]] += 1

        root = -1
        for i in range(n):
            if in_num[i] == 0:
                root = i
                break

        if root == -1:
            return False

        from queue import Queue

        que = Queue()
        existed = set([root])
        que.put(root)
        while not que.empty():
            p = que.get()
            if leftChild[p] != -1:
                if leftChild[p] in existed:
                    return False
                existed.add(leftChild[p])
                que.put(leftChild[p])
            if rightChild[p] != -1:
                if rightChild[p] in existed:
                    return False
                existed.add(rightChild[p])
                que.put(rightChild[p])

        return len(existed) == n


if __name__ == '__main__':
    s = Solution()
    print(s.validateBinaryTreeNodes(10))
