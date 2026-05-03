class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)

        total = sum(nums)

        # Calculate F(0)
        curr = 0
        for i in range(n):
            curr += i * nums[i]

        maximum = curr

        # Calculate remaining rotations
        for i in range(n - 1, 0, -1):

            curr = curr + total - n * nums[i]

            maximum = max(maximum, curr)

        return maximum
