# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        
        # Step 1: Check if there are at least k nodes left
        while temp and count < k:
            temp = temp.next
            count += 1

        if count < k:
            return head  # Not enough nodes to reverse, so return as is

        # Step 2: Reverse first k nodes
        prev = None
        curr = head
        next_node = None
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Recursively call for the rest of the list
        if next_node:
            head.next = self.reverseKGroup(next_node, k)

        # prev is the new head of the reversed k-group
        return prev