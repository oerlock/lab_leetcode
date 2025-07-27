class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        给定一个字符串 s，找出其中不含有重复字符的 最长子串 的长度
        :type s: str
        :rtype: int
        分析：
            分析：
                时间复杂度：O(n)

                空间复杂度：O(min(n, m))，其中 m 是字符集大小（最多 128 个 ASCII 字符）
        """
        # 记录每个字符最后一次出现的位置
        char_index = {}
        rs = 0
        left = 0
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # 窗口左边界，如果发现重复字符，就把 left 移动到重复字符的下一位
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            # 每次都更新最大长度
            rs = max(rs, right - left + 1)
        return rs


if __name__ == '__main__':
    s = Solution()
    # rs_ = s.lengthOfLongestSubstring("bbtablud")
    rs_ = s.lengthOfLongestSubstring("jbpnbwwd")
    print(rs_)
