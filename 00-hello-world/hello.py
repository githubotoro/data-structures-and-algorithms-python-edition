import sys

infile = open("input.txt", "r")
outfile = open("output.txt", "w")

sys.stdin = infile
sys.stdout = outfile


class Solution:
    def __init__(self) -> None:
        pass

    def getGreet(self) -> str:
        _greet = "hello world"
        return _greet


S = Solution()
greet = S.getGreet()
print(greet)


infile.close()
outfile.close()
