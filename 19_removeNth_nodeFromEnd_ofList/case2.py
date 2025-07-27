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
                遍历一次链表，获取链表总长度 L；

                计算出正数第 L - n 个节点位置；

                再次遍历并删除该节点。
        """
        dummy_ = ListNode(-1, head)
        len_ = 0
        while head:
            len_ += 1
            head = head.next
        idx_node2remove = len_ - n

        cur = dummy_
        for _ in range(idx_node2remove):
            cur = cur.next

        cur.next = cur.next.next
        return dummy_.next
