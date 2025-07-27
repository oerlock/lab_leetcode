from collections import Counter


class Solution(object):
    def groupAnagrams(self, strs):
        """
        给定一个字符串数组 strs，将字母异位词（Anagram）分组。
        字母异位词是指字母相同，但排列顺序不同的字符串。
        :type strs: List[str]
        :rtype: List[List[str]]
        分析：
            ✅ 优点：
                能准确处理所有字母异位词；

                使用 Counter 可以自动应对不同字符集（包括 Unicode）；

                frozenset(sorted(...)) 是有效的 hash key 方式。

            ⚠️ 缺点：
                Counter + sorted + frozenset 的开销比直接对字符串排序略大；

                由于 frozenset 是无序集合，虽然你用了 sorted 保证一致性，但还是比 tuple key 慢一些。
        """
        data_ = {}
        for i in strs:
            data_.setdefault(frozenset(sorted(Counter(i).items())), []).append(i)
        return list(data_.values())
