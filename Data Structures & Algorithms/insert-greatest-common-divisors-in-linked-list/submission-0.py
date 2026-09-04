# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        s, f = head, head.next

        while f:

            gcdval = math.gcd(s.val, f.val)

            node = ListNode(gcdval)

            s.next = node
            node.next = f

            s = f
            f = f.next

        return head