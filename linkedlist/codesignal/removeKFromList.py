"""
Link: https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm/description
Category: Linkedlist
Tags:
Solved by: Tarık Taha Uygun
"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    # keep track of linkedlist's head
    head = l
    while l:
        if l.next and l.next.value == k:
            l.next = l.next.next
        else:
            l = l.next
    # if first value is k, we need get rid of it.
    if head and head.value == k:
        return head.next
    else:
        return head


# Test - 1
k = 3
head = ListNode(3)
second = ListNode(1)
head.next = second
third = ListNode(2)
second.next = third
fourth = ListNode(3)
third.next = fourth
fifth = ListNode(4)
fourth.next = fifth
second = ListNode(5)
fifth.next = second

removeKFromList(head, k)
