class Solution(object):
    def reverseVowels(self, s):
        """
        给定一个字符串 s，反转其中所有元音字母的位置。
        :type s: str
        :rtype: str
        """
        tmp_ = list(s)
        left, right = 0, len(tmp_) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while left < right:
            if tmp_[left] not in vowels:
                left += 1
            elif tmp_[right] not in vowels:
                right -= 1
            else:
                tmp_[left], tmp_[right] = tmp_[right], tmp_[left]
                left += 1
                right -= 1
        return ''.join(tmp_)
