class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x > 0 or y > 0:
            x, a = divmod(x, 2)
            y, b = divmod(y, 2)
            if a != b:
                dist += 1
        return dist

    def hammingDistancePlus(self, x: int, y: int) -> int:
        return (bin(x) ^ bin(y)).count(1)


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
