from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        w = len(p) # window length
        n = len(s)
        
        if n < w:
            return [] 

        p_map = {}
        s_map = {}
        res = []

        for i in range(w):
            p_map[p[i]] = p_map.get(p[i], 0) + 1
            s_map[s[i]] = s_map.get(s[i], 0) + 1
        
        if p_map == s_map:
            res = [0]
        
        for j in range(w, n):
            s_map[p[j]] = s_map.get(p[j], 0) + 1
            s_map[p[j - w]] -= 1

            if s_map[p[j - w]] == 0:
                del s_map[p[j - w]]
            
            if s_map == p_map:
                res.append(j - w + 1)

        return res



