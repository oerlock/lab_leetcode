class MinStack(object):
    """
    设计一个支持 push、pop、top 和 getMin 操作的栈，同时要求 getMin 操作能够在常数时间内完成。

    题目描述：
        设计一个支持以下操作的栈：

        push(x): 将元素 x 推入栈中。

        pop(): 移除栈顶元素。

        top(): 获取栈顶元素。

        getMin(): 检索栈中的最小元素。

    要求：
        getMin() 操作必须在常数时间内完成。

    分析：
        优点：
            支持常数时间复杂度 O(1) 查找最小值：通过 self.stack_min 保证栈顶元素始终是最小值。

            支持重复元素：使用 self.counter 记录元素出现次数，确保栈中元素被弹出时，能够正确处理最小值的更新。

        缺点：
            空间复杂度较高：额外使用了一个 self.stack_min 和 self.counter，这些结构会导致空间使用比单纯的栈要多。

            代码逻辑稍复杂(对于相等的最小值)：相较于简单的栈实现，引入了计数器和最小栈，增加了实现的复杂性。
    """

    def __init__(self):
        self.stack = []
        self.stack_min = []
        self.counter = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.stack_min and val < self.stack_min[-1]:
            self.stack_min.append(val)
        if not self.stack_min:
            self.stack_min.append(val)
        self.stack.append(val)
        self.counter[val] = self.counter.get(val, 0) + 1

    def pop(self):
        """
        :rtype: None
        """
        tmp_ = self.stack.pop()
        self.counter[tmp_] -= 1
        if self.counter[tmp_] == 0:
            self.counter.pop(tmp_)
            if tmp_ == self.stack_min[-1]:
                self.stack_min.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
