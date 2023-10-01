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

    def getStages(self) -> list:
        stages = []

        while True:
            try:
                L, H, R = input().split()
                stages.append([int(L), int(H), int(R)])
            except EOFError:
                break

        return stages

    def mergeSkylines(self, leftSkyline: list, rightSkyline: list) -> list:
        i, j = 0, 0
        leftMax, rightMax = 0, 0

        skyline = []

        while i < len(leftSkyline) and j < len(rightSkyline):
            if leftSkyline[i][0] < rightSkyline[j][0]:
                x = leftSkyline[i][0]
                leftMax = leftSkyline[i][1]
                i += 1
            else:
                x = rightSkyline[j][0]
                rightMax = rightSkyline[j][1]
                j += 1

            currMax = max(leftMax, rightMax)

            if not skyline or currMax != skyline[-1][1]:
                skyline.append([x, currMax])

        skyline.extend(leftSkyline[i:])
        skyline.extend(rightSkyline[j:])

        return skyline

    def createSkyline(self, stages: list) -> list:
        if len(stages) == 1:
            L, H, R = stages[0]
            return [(L, H), (R, 0)]

        mid = len(stages) // 2

        leftSkyline = self.createSkyline(stages[:mid])
        rightSkyline = self.createSkyline(stages[mid:])

        mergedSkyline = self.mergeSkylines(leftSkyline, rightSkyline)

        return mergedSkyline

    def formatSkyline(self, skyline: list) -> list:
        formattedSkyline = []

        prevY = 0, 0

        for x, y in skyline:
            if y != prevY:
                if y == 0:
                    formattedSkyline.extend([x])
                else:
                    formattedSkyline.extend([x, y])

                prevY = y

        return formattedSkyline


def main():
    S = Solution()

    stages = S.getStages()
    skyline = S.createSkyline(stages)
    formattedSkyline = S.formatSkyline(skyline)

    pp.pprint(skyline)


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
