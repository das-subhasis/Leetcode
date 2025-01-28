#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # def difference(w1, w2):
        #     diff, n = 0, len(w1)
        #     for i in range(n):
        #         if w1[i] != w2[i]:
        #             diff +=1
        #         if diff > 1:
        #             return False
        #     return True
        
        # n = len(wordList)
        # sol, res = [beginWord], []
        # global minCost 
        # minCost = [float('inf')]
        # cost = 1
        # def backtrack(currentWord = beginWord, cost = 1):
            
        #     if currentWord == endWord:
        #         if cost < minCost[0]:
        #             res.clear()
        #             res.append(sol[:])
        #             minCost[0] = cost
        #         elif cost == minCost[0]:
        #             res.append(sol[:])
        #         return
            
        #     for word in wordList:
        #         if word not in sol and difference(word, currentWord):
        #             sol.append(word)
        #             backtrack(word, cost + 1)
        #             sol.pop()
        
        # backtrack()

        def difference(w1, w2):
            diff, n = 0, len(w1)
            for i in range(n):
                if w1[i] != w2[i]:
                    diff +=1
                if diff > 1:
                    return False
            return diff == 1
        
        wordList = set(wordList)

        if endWord not in wordList:
            return []
        
        queue = deque([(beginWord, [beginWord])])
        visited = set([beginWord])
        res = []
        while queue:
            word, path = queue.popleft()
            
            if word == endWord:
                res.append(path)
                continue

            for wordCheck in wordList:
                if wordCheck not in visited and difference(wordCheck, word):
                    visited.add(wordCheck)
                    queue.append((wordCheck, path + [wordCheck]))
        return res



sol = Solution()

print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# @lc code=end

