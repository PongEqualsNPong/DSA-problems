# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def unlist(l: [ListNode]) -> int:
            if l.next == None:
                return l.val
            else:
                return int(str(unlist(l.next)) + str(l.val))

        def toList(x: int) -> ListNode:
            ls = [int(i) for i in str(x)]

            current = None
            node = None
            for s in ls:
                node = ListNode()
                node.val = s
                node.next = current
                current = node

            return node

        i1 = unlist(l1)
        i2 = unlist(l2)
        i3 = i1 + i2
        print(i1, i2, i3)
        result = toList(i3)
        return result
