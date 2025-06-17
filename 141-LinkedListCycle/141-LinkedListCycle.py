# Last updated: 17/06/2025, 22:14:28
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastNode = head
        slowNode = head
        while fastNode != None and fastNode.next != None:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
            if(slowNode == fastNode):
                return True
        return False

        