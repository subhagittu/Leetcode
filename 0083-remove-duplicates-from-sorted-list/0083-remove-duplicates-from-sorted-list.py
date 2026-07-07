# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        curr = head
        next1 = curr.next

        while curr and next1:
            if curr.val == next1.val:
                curr.next = next1.next
                next1 = curr.next

            else:
                curr = curr.next
                next1 = curr.next

        return head
