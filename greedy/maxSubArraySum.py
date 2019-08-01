
class Solution:
    def maxSubArray(self, nums) -> int:
        max = nums[0]
        for i in range(0, len(nums)):
            sum = nums[i]
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if sum > max:
                    max = sum
        if sum >= max:
            max = sum
        return max


leetCode = Solution()
print(leetCode.maxSubArray([-2, 1]))