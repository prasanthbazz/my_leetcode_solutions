'''
#126
https://leetcode.com/problems/word-ladder-ii/
'''
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        #This dictionary holds list of next words for a given sequence 
        dic = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                tmp = w[:i] + '*' + w[i+1:]
                dic[tmp].append(w)
        max_k = -1
        queue = collections.deque([(beginWord, 0)])
        visited = set()
        self.endWord = endWord
        self.len = len(endWord)
        while queue:
            curr, cnt = queue.popleft()
            for i in range(len(curr)):
                if max_k != -1:
                    break
                tmp = curr[:i] + '*' + curr[i+1:]
                for nxt in dic[tmp]:
                    if nxt == endWord:
                        max_k = cnt+1
                        break
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, cnt+1))
        #endword cannot be reached from beginword
        if max_k == -1:
            return []
        res = []
        seen = {beginWord:max_k+1}
        self.dfs([beginWord], max_k, dic, res, seen)
        return res
    
    def dfs(self, curr, cnt, dic, res, seen):
        if curr[-1] == self.endWord:
            res.append(curr)
            return
        if cnt == 0:
            return
        for i in range(self.len):
            tmp = curr[-1][:i] + '*' + curr[-1][i+1:]
            for w in dic[tmp]:
                #word w was reached earlier in some other path. Hence the current path would not lead to optimal path
                if w in seen and seen[w] > cnt:
                    continue
                seen[w] = cnt
                self.dfs(curr+ [w], cnt - 1, dic, res, seen)
        return