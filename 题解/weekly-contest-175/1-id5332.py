class Solution:
    def checkIfExist(self, arr) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(n):
                if j != i and arr[i] == arr[j] * 2:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
