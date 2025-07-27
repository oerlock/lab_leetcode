class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        给定一个字符串 s 和一个字符串字典 wordDict（一个单词列表），判断 s 是否可以被分割成一个或多个在字典中出现的单词。
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        有问题：
        """
        n = len(wordDict)
        dp = [[0] * (len(s) + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, len(s) + 1):
                if i -1 >= 0:
                    dp[i][j] = dp[i - 1][j]
                if s[j - len(wordDict[i]): j] == wordDict[i] and dp[i][j - len(wordDict[i])] == 1:
                    dp[i][j] = 1

        return bool(dp[-1][-1])
