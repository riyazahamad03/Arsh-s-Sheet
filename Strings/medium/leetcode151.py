class solution:
    def reverseWord(self, s: str):
        res, i, n = "", 0, len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            j = i + 1
            while j < n and s[j] != ' ':
                j += 1
            subStr = s[i: j]
            if len(res) == 0: 
                res = subStr
            else:
                res = subStr + " " + res
            i = j + 1
        return res


x = solution()
print(x.reverseWord( s = "a good   example"))
