import sys
import pprint

infile = open("input.txt", "r")
outfile = open("output.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        pass

    def getStrings(self) -> tuple[str, str]:
        word, text = input().split()

        return word, text

    def bruteForce(self, word: str, text: str) -> bool:
        i = 0
        j = 0
        prev_j = 0

        while i < len(word) and j < len(text):
            if word[i] == text[j]:
                if i == len(word) - 1:
                    return True
                else:
                    i += 1
                    j += 1
            else:
                i = 0
                prev_j += 1
                j = prev_j

        return False

    def kmp(self, word: str, text: str) -> bool:
        cache = [0 for i in range(len(text))]

        i = 0
        j = 1

        while i < len(word):
            if word[i] == text[j]:
                i += 1
                cache[j] = i
                j += 1
            elif i == 0:
                cache[j] = 0
                j += 1
            else:
                i = cache[i - 1]

        i = 0
        j = 0
        prev_j = 0

        while i < len(word) and j < len(text):
            if word[i] == text[j]:
                if i == len(word) - 1:
                    return True
                else:
                    i += 1
                    j += 1
            else:
                if j != 0:
                    j = cache[j - 1]
                else:
                    i += 1

        return False


def main():
    S = Solution()

    word, text = S.getStrings()

    wordExists = S.kmp(word, text)

    print(wordExists)


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
