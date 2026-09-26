class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterMapS = {}
        counterMapT = {}
        for i in range(len(s)):
            counterMapS[s[i]] = 1 + counterMapS.get(s[i], 0)
            counterMapT[t[i]] = 1 + counterMapT.get(t[i], 0)
        
        return counterMapS == counterMapT
