# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        给你一个链表，删除链表的 倒数第 N 个节点，并返回链表的头结点。
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        分析：
            💡 思路：
                设两个指针 fast 和 slow，都从头结点出发。

                fast 先走 n 步；

                然后 fast 和 slow 同时移动；

                当 fast 到达末尾时，slow 刚好指向 待删除节点的前一个节点；

                删除 slow.next 即可。
        """
        dummy_ = ListNode(-1, head)
        fast, slow = dummy_, dummy_
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy_.next
