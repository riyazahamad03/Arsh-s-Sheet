import collections


class solution:
    def groupAnagrams(self, strs: list[str]):
        d = collections.defaultdict(list)
        for strings in strs:
            count = [0] * (26)
            for c in strings:
                count[ord(c) - ord('a')] += 1
            d[tuple(count)].append(strings)
        return d.values()


x = solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
