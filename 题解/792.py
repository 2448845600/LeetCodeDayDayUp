class Solution:
    def numMatchingSubseq(self, S: str, words) -> int:
        hs = {}
        for i in range(len(S)):
            if S[i] in hs:
                hs[S[i]].append(i)
            else:
                hs[S[i]] = [i]

        count = 0
        for word in words:
            left = -1
            word_flag = True
            for c in word:
                if c in hs:
                    clist = hs[c]
                else:
                    word_flag = False
                    break
                if clist[-1] <= left:
                    word_flag = False
                    break
                else:
                    for i in range(len(clist)):
                        if clist[i] > left:
                            left = clist[i]
                            break
            count += word_flag

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
