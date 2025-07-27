from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        给定一个字符串 s，找出其中不含有重复字符的 最长子串 的长度
        :type s: str
        :rtype: int
        分析：
            ❌ 存在的问题：
                效率低下（重复计算）：

                    每次发现重复字符，都重新构建一个 tmp 子串，重新统计频率。

                    这是 O(n²) 的时间复杂度，不符合题目要求的高效解法。

                窗口移动策略混乱：

                    在重复字符时，同时移动左右指针并重新建窗口，违背了滑动窗口的精髓（右指针扩展，左指针收缩）。

                冗余数据结构：

                    max_substring 用来记录字符频率，其实不需要知道频率，只需要知道位置 或是否存在。
        """
        max_substring = {}
        p_l, p_r = 0, 0
        while p_r < len(s):
            if s[p_r] not in max_substring:
                max_substring[s[p_r]] = 1
                p_r += 1
            else:
                while p_r < len(s):
                    p_l += 1
                    p_r += 1
                    tmp = defaultdict(int)
                    for i in s[p_l:p_r+1]:
                        tmp[i] += 1
                    if max(tmp.values()) > 1:
                        continue
                    else:
                        if len(tmp) >= len(max_substring):
                            max_substring = tmp
                            break
                p_r += 1
        return len(max_substring)


if __name__ == '__main__':
    s = Solution()
    # rs_ = s.lengthOfLongestSubstring("bbtablud")
    rs_ = s.lengthOfLongestSubstring("jbpnbwwd")
    print(rs_)
