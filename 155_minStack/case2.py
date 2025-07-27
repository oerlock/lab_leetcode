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
        相等的最小值：
            if not self.stack_min or val <= self.stack_min[-1]:。这样可以保证在多个相等最小值存在时，stack_min 中能够保留最小值出现的次数
    """

    def __init__(self):
        self.stack = []  # 用来存储元素的栈
        self.stack_min = []  # 用来存储当前最小值的栈

    def push(self, val):
        self.stack.append(val)
        if not self.stack_min or val <= self.stack_min[-1]:
            self.stack_min.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.stack_min[-1]:
                self.stack_min.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.stack_min[-1] if self.stack_min else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
