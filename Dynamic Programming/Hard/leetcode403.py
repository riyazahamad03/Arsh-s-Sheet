class Solution:
    def canCross(self, stones: list[int]) -> bool:
        stone_positions = set(stones)
        memo = {}

        def recursive_jump(position, jump_size):
            if position == stones[-1]:
                return True

            if (position, jump_size) in memo:
                return memo[(position, jump_size)]

            for next_jump in [jump_size - 1, jump_size, jump_size + 1]:
                if next_jump > 0 and position + next_jump in stone_positions:
                    if recursive_jump(position + next_jump, next_jump):
                        memo[(position, jump_size)] = True
                        return True

            memo[(position, jump_size)] = False
            return False

        return recursive_jump(0, 0)


x = Solution()
print(x.canCross([0, 1, 3, 5, 6, 8, 12, 17]))
