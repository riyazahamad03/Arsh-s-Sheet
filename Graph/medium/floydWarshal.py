class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != -1 and matrix[k][j] != -1:
                        if matrix[i][j] == -1 or matrix[i][j] > matrix[i][k] + matrix[k][j]:
                            matrix[i][j] = matrix[i][k] + matrix[k][j]

        return matrix


x = Solution()
print(x.shortest_distance(matrix=[
    [0, 1, 43],
    [1, 0, 6],
    [-1, -1, 0]
]))
