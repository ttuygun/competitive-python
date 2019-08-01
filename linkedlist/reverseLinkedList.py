"""
Link: https://leetcode.com/problems/reverse-linked-list/
Category: Linkedlist
Tags:
Site: Leetcode
Solved by: Tarık Taha Uygun
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # track previous ones to update next nodes.
        previous = None
        while head:
            # head.next's updated with previous node so we need to store it.
            next_temp = head.next
            # head's next must points to previous node.
            head.next = previous
            # get next *previous node from current head.
            previous = head
            # get next head node from unchanged temp value
            head = next_temp
        # hereafter, previous node points the head of reversed linked list.
        return previous


t = Solution()
head = ListNode(1)
node_2 = ListNode(2)
head.next = node_2
node_3 = ListNode(3)
node_2.next = node_3
node_4 = ListNode(4)
node_3.next = node_4
node_5 = ListNode(5)
node_4.next = node_5

t.reverseList(head)
