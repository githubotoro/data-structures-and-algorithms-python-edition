class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ""

        for i in range(len(num) - 1, -1, -1):
            curr_digit = int(num[i])

            if curr_digit & 1:
                res += num[: i + 1]
                break

        return res
