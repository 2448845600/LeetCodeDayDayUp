# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = head
        b = head
        c = head

        i = 0
        while c != None:
            i += 1
            c = c.next
            if i > n - 1:
                b = b.next

        b.next = b.next.next
        return a

