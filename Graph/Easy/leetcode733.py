class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ):
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or image[r][c] != start_color
                or (r, c) in visit
            ):
                return
            visit.add((r, c))
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


x = Solution()
print(x.floodFill([[0, 0, 0], [0, 0, 0]], 1, 0 , 0))
