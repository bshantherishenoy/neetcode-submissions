# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_ll(head1, head2):
            cur = dummy = ListNode()
            if not head1:
                return head2
            if not head2:
                return head1
            while head1 and head2:
                if head1.val < head2.val:
                    cur.next = head1
                    head1 = head1.next 
                else:
                    cur.next = head2
                    head2 = head2.next 
                cur = cur.next 
            if head1:
                cur.next = head1
            if head2:
                cur.next = head2
            return dummy.next 
        if not lists:
            return None
        # k^2O(n) 
        # merged = lists[0]
        # for i in range(1, len(lists)):
        #     merged = merge_two_ll(merged , lists[i])
        # k(logk)n
        while len(lists) > 1:
            merge_list = []

            for i in range(0,len(lists),2):
                list1 = lists[i]
                if i+1 < len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None
                merge_list.append(merge_two_ll(list1,list2))
            lists = merge_list
        
        return lists[0]
        