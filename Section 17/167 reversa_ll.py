from ll import LinkedList, Node


# Create a linked list and add elements
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Print the list
ll.print_list()


def reverse_ll(head: Node) -> Node:

    # dummy = Node(0)

    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


res = reverse_ll(ll.head)
while res:
    print(res.data, end=" -> ")
    res = res.next
