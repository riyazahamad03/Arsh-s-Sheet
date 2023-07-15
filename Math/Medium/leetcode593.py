class solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]):
        def getDist(p1, p2):

            return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)**0.5

        distance = [getDist(p1, p2), getDist(p1, p3), getDist(p1, p4),
                    getDist(p2, p3), getDist(p2, p4), getDist(p3, p4)]
        distance.sort()

        if distance[0] == 0:
            return False

        return distance[0] == distance[1] == distance[2] == distance[3] and distance[4] == distance[5]


x = solution()
print(x.validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))
