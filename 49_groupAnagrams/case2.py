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
                不用显式地构造 hash key，逻辑清晰；

                Counter 支持直接比较：两个 Counter 相等，表示字符及其频次完全一致。

            ⚠️ 缺点：
                效率低：

                    if tmp_ not in data_1 需要对 data_1 中的所有 Counter 做逐个比较（等价于 O(n²k)）；

                    data_1.index(tmp_) 同样是线性查找，性能瓶颈严重。

                    无法用作字典 key：

                    Counter 是 dict 的子类，不是 hashable（不能作为 dict key），所以不能用 dict[tmp_]。

                空间浪费：

                    data_1 实际上是“临时中间结果”，占用多余空间。
        """
        data_1 = []
        data_2 = []
        for i in strs:
            tmp_ = Counter(i)
            if tmp_ not in data_1:
                data_1.append(tmp_)
                data_2.append([i])
            else:
                idx = data_1.index(tmp_)
                data_2[idx].append(i)
        return data_2
