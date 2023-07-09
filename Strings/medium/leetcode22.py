class solution:
    def generateParanthesis(self, n: int):
        res, stack = [], []

        def backTrack(openC, closedC):
            if openC == closedC == n:
                res.append("".join(stack))
                return
            if openC < n:
                stack.append('(')
                backTrack(openC + 1, closedC)
                stack.pop()
            if closedC < openC:
                stack.append(')')
                backTrack(openC, closedC + 1)
                stack.pop()

        backTrack(0, 0)
        return res


x = solution()
print(x.generateParanthesis(3))
