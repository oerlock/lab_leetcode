from collections import defaultdict


def sliding_window_variable(s, t):
    """
    最小覆盖子串
    :param s:
    :param t:
    :return:
    """
    # 子串特征（字符频次）
    target_need = defaultdict(int)
    for c in t:
        target_need[c] += 1

    p_l, p_r = 0, 0

    # 符合子串特征的数量（追踪匹配程度）
    valid = 0
    window = defaultdict(int)
    # 初始化为一个无限长的窗口，可以覆盖 s
    rs = (0, float("inf"))
    while p_r < len(s):
        # 新窗口的右边界
        c = s[p_r]
        p_r += 1
        if c in target_need:
            window[c] += 1
            if window[c] == target_need[c]:
                valid += 1

        while valid == len(target_need):  # 在符合所有子串特征的前提下，收缩窗口
            # 取最短的那个窗口
            if p_r - p_l < rs[1] - rs[0]:
                rs = (p_l, p_r)
            # 收缩左边界
            d = s[p_l]
            p_l += 1
            if d in target_need:
                if window[d] == target_need[d]:
                    valid -= 1
                window[d] -= 1
    return s[rs[0]:rs[1]] if rs[1] != float("inf") else ""


s_ = "ADOBECODEBANC"
t_ = "ABC"
print(sliding_window_variable(s_, t_))  # 输出 "BANC"
