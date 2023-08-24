class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line, length = [], 0
        idx = 0

        while idx < len(words):
            if length + len(line) + len(words[idx]) > maxWidth:
                extraSpaces = maxWidth - length
                spaces = extraSpaces // max(1, len(line) - 1)
                rem = extraSpaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if rem:
                        line[j] += " "
                        rem -= 1
                res.append("".join(line))
                line, length = [], 0

            line.append(words[idx])
            length += len(words[idx])

            idx += 1

        lastLine = " ".join(line)
        trailSpace = maxWidth - len(lastLine)
        res.append(lastLine + " " * trailSpace)
        return res


x = Solution()
print(x.fullJustify(words=["This", "is", "an", "example",
      "of", "text", "justification."], maxWidth=16))
