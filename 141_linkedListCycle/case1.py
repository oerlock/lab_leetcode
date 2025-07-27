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
            问题：
                map_[head] = pos：这里只是为了记录节点访问过。其实 pos 无用，改成 map_[head] = True 更清晰。

                Python 中不能直接把 ListNode 作为字典键，除非 ListNode 对象没有重写 __eq__ 和 __hash__。否则建议用 id(head) 做键更稳妥。

                while head.next is not None：应该是 while head is not None。否则在 head 是最后一个节点时会跳过检查最后一个节点是否在环中

            时间复杂度：O(n)，最多遍历一次所有节点。

            空间复杂度：O(n)，最坏情况记录所有节点。
        """
        if head is None:
            return False
        map_ = {}
        pos = -1
        while head.next is not None:
            pos += 1
            if map_.get(head):
                return True
            map_[head] = pos
            head = head.next
        return False
