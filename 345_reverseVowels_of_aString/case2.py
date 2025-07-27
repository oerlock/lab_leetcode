class Solution(object):
    def reverseVowels(self, s):
        """
        给定一个字符串 s，反转其中所有元音字母的位置。
        :type s: str
        :rtype: str
        分析：
            ✅ 核心思想：双指针扫描 + 就地交换
                使用 left 和 right 两个指针分别从字符串的左右两端开始扫描。

                只在两个指针都指向元音时才进行交换。

                元音集合提前定义为 set 类型，查找效率为 O(1)。
            可优化点：
                可以进一步清理逻辑使结构更简洁明了
        """
        tmp_ = list(s)
        left, right = 0, len(tmp_) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while left < right:
            if tmp_[left] not in vowels:
                left += 1
                continue
            if tmp_[right] not in vowels:
                right -= 1
                continue
            if tmp_[left] in vowels and tmp_[right] in vowels:
                tmp_[left], tmp_[right] = tmp_[right], tmp_[left]
            left += 1
            right -= 1
        return ''.join(tmp_)
