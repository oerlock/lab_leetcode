# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        判断一个链表是否有环
        :type head: ListNode
        :rtype: bool
        Floyd 判圈算法
        分析：
            时间复杂度：O(n)

            空间复杂度：O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
