# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while (curr != None):
            # print("looking at curr", curr.val)
            # swap
            temp = curr.next
            # print("temp", temp.val if temp else "n/a")
            # print("prev", prev.val if prev else "n/a")
            curr.next = prev
            # iterate
            prev = curr
            curr = temp
        return prev