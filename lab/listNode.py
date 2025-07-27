class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head: ListNode | None) -> None:
    while head:
        print(head.val)
        head = head.next


def inset2head(val, head: ListNode | None) -> ListNode:
    node_new = ListNode(val, head)
    return node_new


def inset2tail(val, head: ListNode | None) -> ListNode:
    node_new = ListNode(val)
    if not head:
        head = node_new
        return head
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = node_new
    return head


def inset2tail2(val, head: ListNode | None) -> ListNode:
    dummy_ = ListNode(next=head)
    node_new = ListNode(val)
    cur = dummy_
    while cur.next:
        cur = cur.next
    cur.next = node_new
    return dummy_.next


def remove_node(head: ListNode | None, node: ListNode) -> ListNode | None:
    if not head:
        return None

    if head.val == node.val:
        return head.next

    cur = head
    while cur.next:
        if cur.next.val == node.val:
            cur.next = cur.next.next
            break
        cur = cur.next
    return head


def remove_node2(head: ListNode | None, node: ListNode) -> ListNode | None:
    dummy_ = ListNode(next=head)
    cur = dummy_
    while cur.next:
        if cur.next.val == node.val:
            cur.next = cur.next.next
            break
        cur = cur.next
    return dummy_.next
