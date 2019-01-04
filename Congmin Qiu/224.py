class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        dq = deque()

        num = 0
        sign = 1
        res = 0

        for ch in s:
            if ch == " ":
                continue

            if ch == "+":
                res += sign * num
                sign = 1
                num = 0
            elif ch == "-":
                res += sign * num
                sign = -1
                num = 0
            elif ch == "(":
                dq.append(res)
                dq.append(sign)
                res = 0
                sign = 1

            elif ch == ")":
                res += sign * num
                res *= dq.pop()
                res += dq.pop()
                sign = 1
                num = 0
            else:
                num = num * 10 + ord(ch) - ord("0")

        if num != 0:
            res += sign * num
        return res
