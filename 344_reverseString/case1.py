class Solution(object):
    def reverseString(self, s):
        """
        给你一个字符数组 s，请你原地反转这个数组，不能使用额外的数组空间。
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        分析：
        ✅ 优点：
            使用了原地交换（不创建新数组）。

            用了双指针思想：p1 从左向右，p2 从右向左。

            通过 if p1 >= p2: continue 来提前终止不必要的交换。

        ⚠️ 不足：
            for i in range(t) 会遍历整个数组，但只需要遍历一半即可。

            当 i >= t//2 时其实循环已经没必要继续了，即使加了 continue，但循环还是执行了不必要的次数。
        """
        t = len(s)
        for i in range(t):
            p1 = i
            p2 = t - i - 1
            if p1 >= p2:
                continue  # 写错了
            s[p1], s[p2] = s[p2], s[p1]
