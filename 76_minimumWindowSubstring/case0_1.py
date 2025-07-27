from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        给定字符串 s 和 t，要求在 s 中找到包含 t 所有字符的最短子串，返回该子串。如果没有，返回空字符串
        :type s: str
        :type t: str
        :rtype: str
        分析：
            时间复杂度：O(n)
            空间复杂度为 O(m)
        """
        if not s or not t:
            return ""

        # 统计目标字符串 t 中每个字符需要的数量
        target = Counter(t)

        # 还需要匹配的字符总数（包括重复字符）
        missing = len(t)

        # 初始化窗口左右边界，以及最终结果的窗口边界
        start = left = right = 0

        # 枚举 s 中的每个字符，右指针从 1 开始（方便切片）
        for end, char in enumerate(s, 1):
            # 如果当前字符还有未匹配的，missing 减 1
            if target[char] > 0:
                missing -= 1

            # 无论是否需要这个字符，都减少其计数
            target[char] -= 1

            # 当 missing 为 0，说明当前窗口满足条件
            if missing == 0:
                # 尝试收缩左边界，去掉多余的字符
                while start < end and target[s[start]] < 0:
                    target[s[start]] += 1
                    start += 1

                # 更新最小窗口
                if right == 0 or end - start < right - left:
                    left, right = start, end

        # 返回最短窗口子串（右边界是开区间）
        return s[left:right]
