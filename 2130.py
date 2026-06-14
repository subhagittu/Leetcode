# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        half = []
        slow = fast = head

        while fast and fast.next:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        res = 0
        while slow:
            res = max(res, half.pop() + slow.val)
            slow = slow.next

        return res
