class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ha = 0
        ma = 0

        ma = minutes * 6
        ha = (hour % 12) * 30 + minutes / 2

        return min(abs(ma - ha), abs(360 - abs(ma - ha)))


if __name__ == '__main__':
    s = Solution()
    print(s.angleClock(hour=12, minutes=30))
    print(s.angleClock(hour=3, minutes=30))
    print(s.angleClock(hour=3, minutes=15))
    print(s.angleClock(hour=4, minutes=50))
    print(s.angleClock(hour = 12, minutes = 0))
