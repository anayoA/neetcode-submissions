class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(s)
        t_list = sorted(t)
        print(s_list)
        print(t_list)
        return s_list == t_list
        