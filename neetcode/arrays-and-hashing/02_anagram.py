class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = sorted(s)
        t_ = sorted(t)

        return s_ == t_
