class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cache1 = {}
        cache2 = {}

        for i in range(len(s)):
            if s[i] in cache1:
                if cache1[s[i]] != t[i]:
                    return False
            else:
                if t[i] in cache2:
                    return False

                cache1[s[i]] = t[i]
                cache2[t[i]] = s[i]

        return True
