class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        isOpen = 0

        for curr in s:
            if curr == "(":
                isOpen += 1
                if isOpen > 1:
                    res += curr
            else:
                isOpen -= 1
                if isOpen > 0:
                    res += curr

        return res
