# https://oj.leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head
        cur = head
        ne = cur.next
        prev = None
        while not not cur and not not ne:
            tmp = ne.next
            if not prev:
                head = ne
            else:
                prev.next = ne
            prev = cur
            ne.next = cur
            cur.next = tmp
            cur = tmp
            if not cur:
                break
            ne = cur.next
        return head
