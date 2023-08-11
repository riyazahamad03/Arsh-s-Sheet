class solution:
    def uglyNumber(self, n: int):
        uglyList = [1]
        two, three, five = 0, 0, 0
        while len(uglyList) < n:
            by2 = uglyList[two] * 2
            by3 = uglyList[three] * 3
            by5 = uglyList[five] * 5

            mini = min(by2, by3, by5)
            uglyList.append(mini)

            if mini == by2:
                two += 1
            if mini == by3:
                three += 1
            if mini == by5:
                five += 1
        return uglyList[-1]


x = solution()
print(x.uglyNumber(10))
