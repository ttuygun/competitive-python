"""
Link: https://leetcode.com/problems/climbing-stairs
Category: Greedy
Tags: Leetcode
Solved by: Tarık Taha Uygun
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]




leetCode = Solution()
print(leetCode.climbStairs(3))

"""
Test case -  1
Input: 1
1. 1

Ouput: 1

Test case -  2
Input: 2
1. 1 + 1
2. 2

Test case -  3
Input: 3
1. 1 + 1 + 1
2. 2 + 1
3. 1 + 2 

"""