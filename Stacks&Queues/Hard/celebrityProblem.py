class solution:
    def celeb(self, mat: list[list[int]]):
        stack = []
        # adding it to the stack
        for i in range(len(mat)):
            stack.append(i)
        while len(stack) >= 2:
            i1 = stack.pop()
            i2 = stack.pop()

            if mat[i1][i2] == 1:
                # i1 is not celeb
                stack.append(i2)
            else:
                # i2 is not celeb
                stack.append(i1)

        ans = stack.pop()
        for i in range(len(mat)):
            if i != ans:
                if mat[i][ans] == 0 or mat[ans][i]:
                    return -1
        return ans


x = solution()
print(x.celeb([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]))
