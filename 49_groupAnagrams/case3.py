from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        给定一个字符串数组 strs，将字母异位词（Anagram）分组。
        字母异位词是指字母相同，但排列顺序不同的字符串。

        :type strs: List[str]
        :rtype: List[List[str]]
        分析：
        假设有 n 个字符串，每个字符串最长为 k

        排序每个字符串：O(k log k)

        总体时间复杂度：O(n * k log k)

        空间复杂度：O(nk)（用于存储哈希表与结果）
        """
        data_ = defaultdict(list)
        for i in strs:
            data_[tuple(sorted(i))].append(i)
        return list(data_.values())
