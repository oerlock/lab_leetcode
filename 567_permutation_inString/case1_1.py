from collections import defaultdict


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        给定两个字符串 s1 和 s2，判断 s2 中是否存在一个子串是 s1 的排列（即字符组成相同、顺序可以不同）。
        :type s1: str
        :type s2: str
        :rtype: bool
        分析：
            时间复杂度：O(n)，其中 n 是 s2 的长度，每个字符最多进出窗口一次。

            空间复杂度：O(1)，因为字符集是有限的（假设只包含小写字母，固定 26 个）。
        """
        target_need = defaultdict(int)
        for c in s1:
            target_need[c] += 1
        len_ = len(s1)
        valid = 0
        window = defaultdict(int)
        left, right = 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in target_need:
                window[c] += 1
                if window[c] <= target_need[c]:
                    valid += 1

            while valid == len_:
                if right - left == len_:
                    return True
                c = s2[left]
                left += 1
                if c in target_need:
                    if window[c] <= target_need[c]:
                        valid -= 1
                    window[c] -= 1
        return False


if __name__ == '__main__':
    s = Solution()
    s1_ = "abcdxabcde"
    s2_ = "abcdeabcdx"
    print(s.checkInclusion(s1_, s2_))
