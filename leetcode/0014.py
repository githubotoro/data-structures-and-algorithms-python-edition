class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = strs[0]
        largest = strs[0]

        for this_str in strs:
            if this_str <= smallest:
                smallest = this_str
            if this_str >= largest:
                largest = this_str

        res = ""

        for i in range(len(smallest)):
            if smallest[i] == largest[i]:
                res += smallest[i]
            else:
                break

        return res
