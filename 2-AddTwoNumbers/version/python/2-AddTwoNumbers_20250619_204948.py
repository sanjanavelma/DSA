# Last updated: 19/06/2025, 20:49:48
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        # points at the position we are inserting the new digit into
        cur = dummy
        carry = 0
        # iterate through these nodes while either of these has a digit
        while l1 or l2 or carry:
            # think 7 + 8 example
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next


        