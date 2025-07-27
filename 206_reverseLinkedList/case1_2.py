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
            时间复杂度为 O(n)，空间复杂度为 O(n)，因为递归调用会占用额外的栈空间
        """
        # 基本情况：如果链表为空或只有一个节点，直接返回头节点
        if not head or not head.next:
            return head

        # 递归调用：反转链表的剩余部分
        reversed_head = self.reverseList(head.next)

        # 让当前节点变成新尾节点，反转链接
        head.next.next = head
        head.next = None  # 将当前节点的 next 置为 None

        return reversed_head  # 返回反转后的链表头节点


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
