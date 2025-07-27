# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        给你一个链表，删除链表的 倒数第 N 个节点，并返回链表的头结点。
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        分析：
            未完成
        """
        fast = slow = head
        while True:
            for _ in range(n):
                fast = slow.next
            if fast is None or fast.next is None:
                break
            slow = slow.next
        if fast is None:
            head = head.next
        if n == 1:
            slow.next = fast.next if fast else fast
        else:
            slow.next = fast
        return head
