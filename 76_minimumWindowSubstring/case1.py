from collections import defaultdict


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
        target_need = defaultdict(int)
        for c in t:
            target_need[c] += 1

        p_l, p_r = 0, 0
        window = defaultdict(int)
        len_ = len(s)
        rs = (0, len_ + 1)
        valid = 0
        while p_r < len_:
            c = s[p_r]
            p_r += 1
            if c in target_need:
                window[c] += 1
                if window[c] == target_need[c]:
                    valid += 1

            while valid == len(target_need):
                if p_r - p_l < rs[1] - rs[0]:
                    rs = (p_l, p_r)

                c = s[p_l]
                p_l += 1
                if c in target_need:
                    if window[c] == target_need[c]:
                        valid -= 1
                    window[c] -= 1

        return s[rs[0]:rs[1]] if rs[1] < len_ + 1 else ""


if __name__ == '__main__':
    s = Solution()
    s_ = "ADOBECODEBANC"
    t_ = "ABC"
    rs_ = s.minWindow(s_, t_)
    print(rs_)
