from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def print(head):
        while head:
            print(head.val, end="->")
            head = head.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        while head:
            temp_node = head.next
            head.next = prev_node
            prev_node = head
            head = temp_node

        return prev_node

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        p1, p2 = list1, list2
        head = None

        while p1 and p2:
            if p1.val <= p2.val:
                if head is None:
                    head = p1

                temp_node = p1.next
                p1.next = p2
                p1 = temp_node

            else:
                if head is None:
                    head = p2

                temp_node = p2.next
                p2.next = p1
                p2 = temp_node

        return head


# First sorted linked list: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Second sorted linked list: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

sol = Solution()
res = sol.mergeTwoLists(list1, list2)
ListNode.print(res)
