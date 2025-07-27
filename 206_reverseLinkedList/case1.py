# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next.val if self.next else "None"}'


class Solution(object):
    def reverseList(self, head):
        """
        反转一个单链表
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        分析：
            时间复杂度：
                每个节点仅被访问一次，所以时间复杂度是 O(n)，其中 n 是链表的节点数。

            空间复杂度：
                只使用了常数级的额外空间，所以空间复杂度是 O(1)。
        """
        next_ = None
        while head:
            tmp = head.next
            next_, head.next = head, next_
            head = tmp
        return next_


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    node = s.reverseList(node1)

    while node:
        print(node)
        node = node.next
