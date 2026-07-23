# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy= ListNode(0)
        dummy.next = head 

        cur = head 
        listprev = dummy 

        for _ in range(left-1):
            listprev= cur
            cur= cur.next

        revstart = cur
        prev = None
        for _ in range(right - left + 1):
            newnode = cur.next
            cur.next = prev
            prev = cur 
            cur = newnode
        listprev.next = prev
        revstart.next = cur
        return dummy.next
