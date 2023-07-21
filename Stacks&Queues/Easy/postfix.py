class solution:
    def postFix(self, exp: str):
        stack = []
        for i in range(len(exp)):
            if exp[i] == '+':
                val2 = stack.pop()
                val1 = stack.pop()

                stack.append(val1 + val2)
            elif exp[i] == '-':
                val2 = stack.pop()
                val1 = stack.pop()

                stack.append(val1 - val2)
            elif exp[i] == '*':
                val2 = stack.pop()
                val1 = stack.pop()

                stack.append(val1 * val2)
            elif exp[i] == '/':
                val2 = stack.pop()
                val1 = stack.pop()

                stack.append(val1//val2)

            else:
                if exp[i].isdigit():
                    stack.append(int(exp[i]))
        return stack[-1]


x = solution()
print(x.postFix("231*+9-"))
