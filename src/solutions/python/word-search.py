'''
#79
https://leetcode.com/problems/word-search/
'''
class Solution(object)
    def exist(self, board, word)
        
        type board List[List[str]]
        type word str
        rtype bool
        
        seen = [[False for j in range(len(board[0]))] for i in range(len(board))]
        self.directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(len(board))
            for j in range(len(board[0]))
                if self.canWordFormed(board, i, j, word, 0, seen)
                    return True
        return False

    def canWordFormed(self, board, i, j, word, curr, seen)
        if curr == len(word)
            return True
        if i  0 or i == len(board) or j  0 or j == len(board[0]) or seen[i][j] or board[i][j] != word[curr]
            return False
        seen[i][j] = True
        for d in self.directions
            if self.canWordFormed(board, i+d[0], j+d[1], word, curr+1, seen)
                return True
        seen[i][j] = False
        return False