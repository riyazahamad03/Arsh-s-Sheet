class solution:
    def simplifyPath(self, path: str):
        stack = []
        curr = ""

        for ch in path + "/":
            if ch == '/':
                if curr == "..":
                    if stack:
                        stack.pop()
                elif not (curr == '.' or not curr):
                    stack.append(curr)
                curr = ""
            else:
                curr += ch
        return "/" + "/".join(stack)


x = solution()
print(x.simplifyPath(path="/home/"))
