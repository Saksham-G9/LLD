from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        # find length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr = head

        while length >= k:
            prev = None
            group_tail = curr

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # connect previous group with reversed head
            prev_group_tail.next = prev
            # connect tail of reversed group to next group's head
            group_tail.next = curr

            # move prev_group_tail forward
            prev_group_tail = group_tail

            length -= k

        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
k = 4

sol = Solution().reverseKGroup(n1, k)
print(sol)
while sol:
    print(sol.val, end="-> ")
    sol = sol.next
