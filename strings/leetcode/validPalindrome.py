"""
Link: https://leetcode.com/problems/valid-palindrome
Category: Strings
Tags:
Solved by: Tarık Taha Uygun
"""


class Solution:
    # Keep only numbers and English letters from input
    def keepAlnum(self, input: str) -> str:
        return ''.join(filter(str.isalnum, input))

    def isPalindrome(self, s: str) -> bool:
        s = self.keepAlnum(s).lower()
        len_s = len(s)

        # Example: yapay
        # i = 0, y == y
        # i = 1, a == a
        # You do not need to check if string is odd
        for i in range(0, int(len_s / 2)):
            # -1 is the condition of accessing the last element in array.
            # len_s - i is the other condition of comparing from last to first along in a loop.
            if s[i] == s[len_s - i - 1]:
                pass
            #
            else:
                return False
        return True


leetCode = Solution()
print(leetCode.isPalindrome("race a car"))