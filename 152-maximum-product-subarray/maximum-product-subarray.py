class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        ans = nums[0]
        best = nums[0]
        worst = nums[0]

        for i in range(1, n):
            x = nums[i]

            a = x * best
            b = x * worst
            c = x

            best = max(a, b, c)
            worst = min(a, b, c)

            ans = max(ans, best)

        return ans