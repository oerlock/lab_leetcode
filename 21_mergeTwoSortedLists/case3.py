# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        你将得到两个升序的链表 list1 和 list2 的头节点。
        请将它们合并成一个升序链表，并返回新链表的头节点。

        链表需要通过拼接原有节点的方式来合并。
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        分析：
            迭代的写法
        """
        dummy = ListNode(-1)
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next
