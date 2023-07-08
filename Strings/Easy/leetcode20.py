class solution:
    def isValid(self, s: str):
        d = {')': '(', '}': '{', '[': ']'}
        stack = []
        for i in s:
            if i in d:
                if stack and stack[-1] == d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True


x = solution()
print(x.isValid(s="()"))
