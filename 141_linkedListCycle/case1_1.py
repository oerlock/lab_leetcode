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
        分析：
            时间复杂度：O(n)，最多遍历一次所有节点。

            空间复杂度：O(n)，最坏情况记录所有节点。
        """
        visited = set()
        while head is not None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
