# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # this is uses finding the mid point
        # get  the reverse 
        # merge the sorted array
        slow , fast = head, head.next
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next
        
        second = slow.next
        slow.next = None 

        # Get the reverse :
        prev = None 
        cur = second
        while cur:
            NextNode = cur.next 
            cur.next = prev
            prev = cur 
            cur = NextNode
        second = prev 
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first =  temp1
            second = temp2
        