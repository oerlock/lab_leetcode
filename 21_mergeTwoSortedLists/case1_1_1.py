# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None, label=''):
        self.val = val
        self.next = next
        self.label = label

    def __repr__(self):
        return f'({self.label}){self.val}'
        # return f'({self.label}){self.val} -> ({self.next.label if self.next else "None"}){self.next.val if self.next else "None"}'


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
            有思路了，但实现逻辑迷糊
        """
        pre = ListNode()
        cur = pre
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
        return pre.next


# if __name__ == '__main__':
#     a_1 = ListNode(1, label='a')
#
#     b_1 = ListNode(2, label='b')
#
#     s = Solution()
#     node = s.mergeTwoLists(a_1, b_1)
#
#     while node:
#         print(node)
#         node = node.next
if __name__ == '__main__':
    a_1 = ListNode(1, label='a')
    a_2 = ListNode(2, label='a')
    a_3 = ListNode(4, label='a')
    a_1.next = a_2
    a_2.next = a_3

    b_1 = ListNode(1, label='b')
    b_2 = ListNode(3, label='b')
    b_3 = ListNode(4, label='b')
    b_1.next = b_2
    b_2.next = b_3

    s = Solution()
    node = s.mergeTwoLists(a_1, b_1)

    while node:
        print(node)
        node = node.next
