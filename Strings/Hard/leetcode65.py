class solution:
    def isNumber(self, s: str):
        digitSeen, eSeen, dotSeen = False, False, False
        countPlusMinus = 0
        for i in range(len(s)):
            if s[i].isdigit():
                digitSeen = True
            elif s[i] in ['+', '-']:
                if countPlusMinus == 2:
                    return False
                if i > 0 and (s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
                if i == len(s) - 1:
                    return False
                countPlusMinus += 1

            elif s[i] == '.':
                if eSeen or dotSeen:
                    return False
                if i == len(s) - 1 and not digitSeen:
                    return False
                dotSeen = True
            elif s[i] in ['e', 'E']:
                if eSeen or not digitSeen or i == len(s) - 1:
                    return False
                eSeen = True
            else:
                return False
        return True


x = solution()
print(x.isNumber("e"))
