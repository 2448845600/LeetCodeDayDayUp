class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        n, rmax = len(intervals), 0
        for _, right in intervals:
            if right <= rmax:
                n = n - 1
            else:
                rmax = right
        return n

    def removeCoveredIntervalsPlus(self, intervals) -> int:
        n, rmax = 0, 0
        for _, right in sorted(intervals, key=lambda x: (x[0], -x[1])):
            if right > rmax:
                n = n + 1
                rmax = right
        return n


if __name__ == '__main__':
    s = Solution()
    print(s.removeCoveredIntervals([[3, 10], [4, 10], [5, 11]]))
