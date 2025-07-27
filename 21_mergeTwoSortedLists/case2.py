# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
            ✅ 递归的优点：
                写法简洁、直观

                易于理解（特别适合链表这种“天然递归”的结构）

            ⚠️ 注意：
                递归深度过大（链表太长）时，可能会造成栈溢出。

                Python 的递归深度默认限制是 1000，可以用 sys.setrecursionlimit 调整（但不推荐随便改）。
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
