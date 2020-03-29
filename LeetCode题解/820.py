class Solution:
    def minimumLengthEncoding(self, words) -> int:
        words = sorted(list(map(lambda s: s[::-1], set(words))))
        ans = [words[-1]]
        for i in range(len(words) - 1):
            if words[i] not in words[i + 1]:
                ans.append(words[i])
        return sum([len(_) + 1 for _ in ans])


if __name__ == '__main__':
    s = Solution()
    print(s.minimumLengthEncoding(words=["time", "me", "bell"]))
