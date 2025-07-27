class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        给定一个字符串 s 和一个字符串字典 wordDict（一个单词列表），判断 s 是否可以被分割成一个或多个在字典中出现的单词。
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        思路解析（动态规划）
            1、状态定义：
                dp[i]：字符串 s[0:i]（前 i 个字符）是否可以被拆分为一个或多个字典单词
            2、转移方程：
                找一个 j，使得 dp[j] == True，并且 s[j:i] 是字典中的单词
                    dp[i] = dp[j] and s[j:i] in wordDict for some j in [0, i)
            3、初始化：
                空字符串可以被拆分：dp[0] = True
        分析：
            复杂度：
                时间： O(n^2)，n 是字符串长度。嵌套两个循环。

                空间： O(n)，用于 dp 数组。
        """
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True

        return dp[-1]
