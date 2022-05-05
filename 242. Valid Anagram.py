class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        if len(dict_s.keys()) != len(dict_t.keys()):
            return False

        for key in dict_s.keys():
            if dict_s[key] != dict_t.get(key, 0):
                return False
        
        return True