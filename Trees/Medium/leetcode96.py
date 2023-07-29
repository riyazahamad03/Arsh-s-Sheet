class solution:
    def numTrees(self, n: int):
        numTree = [1] * (n + 1)

        for node in range(2, n + 1):
            tot = 0
            for root in range(1, node + 1):
                left, right = root - 1, node - root
                tot += numTree[left] * numTree[right]
            numTree[node] = tot
        return numTree[n]


x = solution()
print(x.numTrees(3))
