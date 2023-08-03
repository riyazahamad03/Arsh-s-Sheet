from collections import deque


class Solution:
    def minStepsToReachTarget(self, knightPos, TargetPos, N):
        tr, tc = TargetPos
        directions = [
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (-2, -1),
            (-2, 1),
            (2, -1),
            (2, 1),
        ]

        queue = deque([(knightPos[0], knightPos[1], 0)])
        visited = set([(knightPos[0], knightPos[1])])

        while queue:
            r, c, steps = queue.popleft()

            if r == tr and c == tc:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 1 <= nr <= N and 1 <= nc <= N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1


x = Solution()
print(x.minStepsToReachTarget([4, 5], [1, 1], 6))
