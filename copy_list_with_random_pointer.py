from typing import Optional, List


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def build_linked_list(arr: List[List[Optional[int]]]) -> Optional[Node]:
    if not arr:
        return None

    # Step 1: Create nodes without random
    nodes = [Node(val) for val, _ in arr]

    # Step 2: Link next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Step 3: Link random pointers
    for i, (_, rand_index) in enumerate(arr):
        if rand_index is not None:
            nodes[i].random = nodes[rand_index]

    return nodes[0]  # return head


head_data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = build_linked_list(head_data)

curr = head
while curr:
    rand_val = curr.random.val if curr.random else None
    print(f"Node({curr.val}) -> random({rand_val})")
    curr = curr.next

print("=" * 20)


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Map original nodes → copied nodes
        mapping = {}

        dummy = Node(0)
        copy_curr = dummy
        orig_curr = head

        while orig_curr:
            new_node = Node(orig_curr.val)
            mapping[orig_curr] = new_node
            copy_curr.next = new_node

            orig_curr = orig_curr.next
            copy_curr = copy_curr.next

        # Pass 2: Copy random pointers
        orig_curr, copy_curr = head, dummy.next
        while orig_curr:
            if orig_curr.random:
                copy_curr.random = mapping[orig_curr.random]
            orig_curr = orig_curr.next
            copy_curr = copy_curr.next

        return dummy.next


sol = Solution()
res = sol.copyRandomList(head)
curr = res
while curr:
    rand_val = curr.random.val if curr.random else None
    print(f"Node({curr.val}) -> random({rand_val})")
    curr = curr.next
