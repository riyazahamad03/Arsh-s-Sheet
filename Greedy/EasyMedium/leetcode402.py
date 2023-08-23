class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for c in nums:
            while stack and k > 0 and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        stack = stack[:len(stack) - k]
        res = "".join(stack).lstrip("0") 
        return str(int(res)) if res else "0"
x = Solution()
print(x.removeKdigits(nums = "1432219", k = 3))