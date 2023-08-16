class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:

        if sum(nums) % k:
            return False
        nums.sort(reverse=True)

        tar = sum(nums)/k
        used = [False] * len(nums)

        def backTrack(idx, k, sumVal):
            if k == 0:
                return True
            if sumVal == tar:
                return backTrack(0, k - 1, 0)

            for j in range(idx, len(nums)):
                if j > 0 and not used[j-1] and nums[j] == nums[j - 1]:
                    continue

                if used[j] or sumVal + nums[j] > tar:
                    continue
                used[j] = True

                if backTrack(j + 1, k, sumVal + nums[j]):
                    return True
                used[j] = False
            return False
        return backTrack(0, k, 0)


x = Solution()
print(x.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
