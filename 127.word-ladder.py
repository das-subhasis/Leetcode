#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def difference(w1, w2):
            diff, n = 0, len(w1)
            for i in range(n):
                if w1[i] != w2[i]:
                    diff +=1
                if diff > 1:
                    return False
            return True
        
        n = len(wordList)
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            word, cost = queue.popleft()
            
            if word == endWord:
                return cost
            
            for wordCheck in wordList:
                if wordCheck not in visited and difference(wordCheck, word):
                    queue.append((wordCheck, cost + 1))
                    visited.add(wordCheck)
        return 0

# @lc code=end

