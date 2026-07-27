# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getkth(groupprev,k):
            cur = groupprev
            while cur  and k>0:
                cur = cur.next 
                k -=1
            return cur
        
        dummy = ListNode(0)
        dummy.next = head 
        groupprev = dummy
        while True:
            kth = getkth(groupprev,k)
            if not kth:
                break
            groupnext = kth.next
            prev = groupnext
            cur = groupprev.next
            while cur != groupnext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp
        return dummy.next

