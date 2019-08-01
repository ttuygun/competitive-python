"""
Link: https://leetcode.com/problems/valid-anagram
Category: Strings
Tags:
Site: Leetcode
Solved by: Tarık Taha Uygun
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a hash table in order to recurrence of each character in s.
        sozluk = {}

        # Build hash table.
        for i in s:
            if i not in sozluk.keys():
                sozluk[i] = 1
            else:
                sozluk[i] += 1

        # Decrement the count of each character in t.
        for i in t:
            # If any character which cannot be found in sozluk's keys, you must return immediately false.
            if i not in sozluk.keys():
                return False
            # If you found a character in sozluk's keys, you must decrement it.
            else:
                sozluk[i] -= 1

        # Accepted anagram condition
        for i in sozluk.values():
            if i != 0:
                return False
        return True


leetCode = Solution()
print(leetCode.isAnagram("anagram", "nagaram"))