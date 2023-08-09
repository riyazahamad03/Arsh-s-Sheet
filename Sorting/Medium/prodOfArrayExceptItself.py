class solution:
    def productOfArrayExceptItself(self, arr: list[int]):
        n = len(arr)
        prefixProd, postfixProd = [1] * (n), [1] * (n)

        # populating prefix
        pre = 1
        for i in range(n):
            prefixProd[i] = pre
            pre = pre * arr[i]

        # populating postfix
        post = 1
        for i in range(n - 1, - 1, - 1):
            postfixProd[i] = post
            post = post * arr[i]

        res = [1] * (n)
        for i in range(n):
            res[i] = prefixProd[i] * postfixProd[i]
        return res


x = solution()
print(x.productOfArrayExceptItself([10, 3, 5, 6, 2]))
