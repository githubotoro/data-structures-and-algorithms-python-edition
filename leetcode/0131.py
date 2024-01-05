class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        substring = s[left : right + 1]

        if substring in self.cache:
            return self.cache[substring]

        self.cache[substring] = True

        while left <= right:
            if s[left] != s[right]:
                self.cache[substring] = False
                break

            left += 1
            right -= 1

        return self.cache[substring]

    def recurse(
        self, s: str, curr: int, substrings: List[str], res: List[List[str]]
    ) -> None:
        if curr == len(s):
            res.append(substrings.copy())
            return

        for ptr in range(curr, len(s)):
            if self.isPalindrome(s, curr, ptr):
                substrings.append(s[curr : ptr + 1])

                self.recurse(s, ptr + 1, substrings, res)

                substrings.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = []

        self.recurse(s, 0, [], res)

        return res
