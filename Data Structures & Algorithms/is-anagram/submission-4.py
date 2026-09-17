class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = sorted(list(s))
        tList = sorted(list(t))
        return sList == tList