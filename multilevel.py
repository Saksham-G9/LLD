from collections import deque
from typing import Optional


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def build_multilevel_list(data):
    """Build multilevel doubly linked list from LeetCode 430 array format."""
    if not data:
        return None

    # queue of (parent, child_head)
    q = deque()
    dummy = Node(0)
    prev = dummy
    head = None

    i = 0
    while i < len(data):
        if data[i] is None:  # end of current level
            if q:
                parent, child_head = q.popleft()
                parent.child = child_head
                prev = parent  # reset prev to parent so linking continues correctly
            i += 1
            continue

        # create node
        node = Node(data[i])
        if not head:
            head = node

        # link prev <-> node
        prev.next = node
        node.prev = prev
        prev = node

        # if next value is not None, continue; otherwise prepare child queue
        if i + 1 < len(data) and data[i + 1] is None:
            q.append((node, None))  # placeholder, will be fixed when child starts
        elif q and q[-1][1] is None:
            # fill in child's head when first real node after null appears
            parent, _ = q.pop()
            q.append((parent, node))

        i += 1

    return head


def print_multilevel_list(head):
    def dfs(node, level):
        curr = node
        while curr:
            print("  " * level + f"{curr.val}")
            if curr.child:
                dfs(curr.child, level + 1)
            curr = curr.next

    dfs(head, 0)


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        def dfs(node: Node) -> Node:
            curr = node
            last = node  # tail of the flattened list

            while curr:
                next_node = curr.next

                # If there is a child, recurse
                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    # Connect curr → child
                    curr.next = child_head
                    child_head.prev = curr

                    # Connect child's tail → next_node
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    # Clear child pointer
                    curr.child = None

                    last = child_tail
                else:
                    last = curr

                curr = next_node

            return last  # return tail of this segment

        dfs(head)
        return head


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3
    n4.next = n5
    n5.prev = n4
    n5.next = n6
    n6.prev = n5

    # Level 2
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)

    n7.next = n8
    n8.prev = n7
    n8.next = n9
    n9.prev = n8
    n9.next = n10
    n10.prev = n9

    n3.child = n7  # link child of 3 → 7

    # Level 3
    n11 = Node(11)
    n12 = Node(12)

    n11.next = n12
    n12.prev = n11

    n8.child = n11

    sol = Solution()
    flat_head = sol.flatten(n1)
    print("\nFlattened list:")
    curr = flat_head
    while curr:
        print(curr.val, end=" → ")
        curr = curr.next
