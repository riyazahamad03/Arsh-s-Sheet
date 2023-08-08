import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pat = word[:j] + "*" + word[j+1:]
                nei[pat].append(word)
        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pat = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pat]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0


x = Solution()
print(x.ladderLength(beginWord="hit", endWord="cog",
      wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
