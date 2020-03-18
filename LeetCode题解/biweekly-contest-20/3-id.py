class Solution:
    def numberOfSubstringsNaive(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            exist = '' + s[i]
            j = i + 1
            while len(exist) < 3 and j < n:
                if s[j] not in exist:
                    exist += s[j]
                j += 1

            if len(exist) == 3:
                count += 1 + n - j

        return count

    def numberOfSubstrings(self, s: str) -> int:
        import bisect
        count = 0
        n = len(s)
        apos = []
        bpos = []
        cpos = []
        for i in range(n):
            if s[i] == 'a':
                apos.append(i)
            elif s[i] == 'b':
                bpos.append(i)
            else:
                cpos.append(i)

        for i in range(n):
            exist = '' + s[i]
            j = i + 1
            while len(exist) < 2 and j < n:
                if s[j] not in exist:
                    exist += s[j]
                j += 1

            j = j - 1
            if 'a' not in exist:
                k = bisect.bisect_right(apos, j)
                if k < len(apos):
                    exist += 'a'
                    count += n - apos[k]
            elif 'b' not in exist:
                k = bisect.bisect_right(bpos, j)
                if k < len(bpos):
                    exist += 'b'
                    count += n - bpos[k]
            else:
                k = bisect.bisect_right(cpos, j)
                if k < len(cpos):
                    exist += 'c'
                    count += n - cpos[k]

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubstrings("abcabc"))
    print(s.numberOfSubstrings("aaacb"))
    print(s.numberOfSubstrings("abc"))
