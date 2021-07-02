"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

It is guaranteed that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.



Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
"""

# Two other methods other than this optimal solution
# brute force to iterate through the list multiple times
# or using hashset as below
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashset = set()
        while headA:
            hashset.add(headA)
            headA = headA.next
        while headB:
            if headB in hashset:
                return headB
            headB = headB.next
        return None



# Next method uses the fact that the intersection can only happen at a point in the shorter list
# So, taking the pointer on the longer list to the point where len(longer) - len(shorter)
# then comparing the lists at each node
class Solution:
    def getSize(self, head):
        curr = head
        count = 0
        while (curr):
            count += 1
            curr = curr.next
        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        size_A = self.getSize(headA)
        size_B = self.getSize(headB)

        for i in range(abs(size_A - size_B)):
            if (size_A > size_B):
                headA = headA.next
            else:
                headB = headB.next

        while (headA and headB):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return



# Modified version of the above approach
# instead of getting lenghts of both the lists
# two pointers iterate through both
# atleast by second round they will reach the intersection of nodes, if exist
# 1 represents list 1
# 2 represents list 2 and 'm' represnts merge
# 1111mm222m
# 222m1111mm
# We are able to see that at the last index of both the pointers, we identify the node where merge starts
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA