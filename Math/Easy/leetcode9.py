class Solution:
    def isPalindrome(self, x: int):
        divider = 1
        while x >= divider * 10:
            divider *= 10
        while x:
            l = x % 10
            r = x//divider

            if l != r:
                return False
            x = (x % divider)//10
            divider //= 100
        return True


x = Solution()
print(x.isPalindrome(121121))
