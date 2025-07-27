class Solution(object):
    def reverseVowels(self, s):
        """
        给定一个字符串 s，反转其中所有元音字母的位置。
        :type s: str
        :rtype: str
        分析：
            时间复杂度：O(n)：一次遍历提取元音索引 + 一次遍历交换位置。
            空间复杂度 O(n)：额外用了一个列表来保存索引。
        """
        tmp_ = list(s)
        data_ = []
        data_1 = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for idx, val in enumerate(tmp_):
            if val in data_1:
                data_.append(idx)
        for idx in range(len(data_) // 2):
            tmp_[data_[idx]], tmp_[data_[-idx - 1]] = tmp_[data_[-idx - 1]], tmp_[data_[idx]]
        return ''.join(tmp_)


if __name__ == '__main__':
    s = Solution()
    rs = s.reverseVowels("IceCreAm")
    print(rs)
