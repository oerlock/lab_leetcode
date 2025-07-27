class Solution(object):
    def isAnagram(self, s, t):
        """
        给定两个字符串 s 和 t，编写一个函数判断它们是否是字母异位词（Anagram）。

        字母异位词 是指由相同字母组成，但排列顺序不同的字符串。
        :type s: str
        :type t: str
        :rtype: bool
        分析：
            ⚠️ 潜在问题/不够简洁的地方
                if data_[i] <= 0: 后 pop(i) 有点不直观，如果字符数恰好为 0 就提前删掉，其实可以等最后统一判断。

                有点“聪明过头”，增加了理解成本。

                比较繁琐，不如 Pythonic 的写法简洁。
        """
        data_ = {}
        for i in s:
            data_[i] = data_.get(i, 0) + 1
        for i in t:
            data_[i] = data_.get(i, 0) - 1
            if data_[i] <= 0:
                tmp_ = data_.pop(i)
                if tmp_ < 0:
                    return False
        if data_:
            return False
        return True
