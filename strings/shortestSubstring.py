"""
Category: Strings
Tags:
Solved by: Tarık Taha Uygun
Problem: Given a string comprised of lowercase letters in the range ascii[a-z], determine the length of the smallest substring that contains all of the letters present in the string.
"""


def shortestSubstring(str):
    n = len(str)
    distinct_count = len(set(str))

    smallest = 10**5

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = str[i: j]
            distinct_substring = set(substring)
            len_substring = len(substring)
            distinct_substring_count = len(distinct_substring)
            if distinct_substring_count == distinct_count:
                if len_substring == distinct_count:
                    return len_substring
                if len_substring < smallest:
                    smallest = len_substring
    return smallest


print(shortestSubstring("dabbcabcd") == 4)
print(shortestSubstring("bab") == 2)
print(shortestSubstring("bcaacbc") == 3)
