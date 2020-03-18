class Solution:

    def minSteps(self, s: str, t: str) -> int:
        sa = {}
        ta = {}
        for c in s:
            if c in sa.keys():
                sa[c] += 1
            else:
                sa[c] = 1

        for c in t:
            if c in ta.keys():
                ta[c] += 1
            else:
                ta[c] = 1

        count = 0
        for key in sa.keys():
            if key in ta.keys():
                if sa[key] > ta[key]:
                    count += sa[key] - ta[key]
            else:
                count += sa[key]

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.minSteps(s="leetcode", t="practice"))
