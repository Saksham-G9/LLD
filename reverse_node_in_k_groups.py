from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # calculating size of ll

        curr_node = head
        len_ll = 0
        while curr_node:
            len_ll += 1
            curr_node = curr_node.next

        # returning in case k is > len of ll
        if len_ll < k:
            return head

        curr_node = head

        # prev_node = None

        prev_tail = None
        new_head = None

        while curr_node:
            prev_node = None
            new_tail = curr_node

            if len_ll < k:
                break

            for _ in range(k):

                temp = curr_node.next

                curr_node.next = prev_node

                prev_node = curr_node

                curr_node = temp

            len_ll -= k

            new_tail.next = curr_node
            # prev_node = new_tail 

            if new_head is None:
                new_head = prev_node

            if prev_tail:
                prev_tail.next = prev_node

            prev_tail = new_tail

        return new_head


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
