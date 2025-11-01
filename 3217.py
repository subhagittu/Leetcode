# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d=Counter(nums)
        t=head
        p=head
        while t!=None:
            if d[t.val]:
                if t==head:
                    head=t.next
            
                else :
                    p.next=t.next
            else:
                p=t
            t=t.next
        return head
                
