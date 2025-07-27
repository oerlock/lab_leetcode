from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        """
        给定两个字符串 s 和 p，找到所有 p 的 异位词 在 s 中出现的位置，返回它们的起始索引。
        :type s: str
        :type p: str
        :rtype: List[int]
        分析：
            时间复杂度：O(n)
            空间复杂度：O(1)
        """
        target_need = defaultdict(int)
        for c in p:
            target_need[c] += 1

        valid = 0
        window = defaultdict(int)
        rs = []
        p_l, p_r = 0, 0
        while p_r < len(s):
            c = s[p_r]
            p_r += 1
            if c in target_need:
                window[c] += 1
                if window[c] <= target_need[c]:
                    valid += 1

            while valid == len(p):
                if p_r - p_l == len(p):
                    rs.append(p_l)

                c = s[p_l]
                p_l += 1
                if c in target_need:
                    if window[c] <= target_need[c]:
                        valid -= 1
                    window[c] -= 1
        return rs


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))