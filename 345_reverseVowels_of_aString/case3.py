class Solution(object):
    def reverseVowels(self, s):
        """
        给定一个字符串 s，反转其中所有元音字母的位置。
        :type s: str
        :rtype: str
        """
        tmp_ = list(s)
        vowels = set('aeiouAEIOU')
        left, right = 0, len(tmp_) - 1
        while left < right:
            while left < right and tmp_[left] not in vowels:
                left += 1
            while left < right and tmp_[right] not in vowels:
                right -= 1
            tmp_[left], tmp_[right] = tmp_[right], tmp_[left]
            left += 1
            right -= 1
        return ''.join(tmp_)
