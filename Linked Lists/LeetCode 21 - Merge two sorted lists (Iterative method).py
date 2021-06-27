"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.



Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1

        if (l1 and l2):
            if l1.val <= l2.val:
                sort = l1
                l1 = sort.next
            else:
                sort = l2
                l2 = sort.next
        new_head = sort
        if l1==None:
            new_head.next = l2
            return new_head
        elif l2==None:
            new_head.next = l1
            return new_head

        while(l1 and l2):
            if (l1.val <= l2.val):
                sort.next = l1
                sort = l1
                l1= sort.next

            else:
                sort.next = l2
                sort = l2
                l2 = sort.next

            if (l1 == None):
                sort.next = l2
            if l2 == None:
                sort.next = l1

        return new_head