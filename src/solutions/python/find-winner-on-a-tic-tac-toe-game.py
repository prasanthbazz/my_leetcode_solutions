"""
#1275
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
"""
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        self.moves = moves
        self.rowCnt = [0] * 3
        self.colCnt = [0] * 3
        self.lDiag = 0
        self.rDiag = 0
        player = 1
        for i in moves:
            self.recordMove(player, i[0], i[1])
            player *= -1
        res = self.findResult()
        res_list = ["Draw","A","B","Pending"]
        try:
            return res_list[res]
        except KeyError:
            return None

    def recordMove(self, player, i, j):
        self.rowCnt[i] += player
        self.colCnt[j] += player
        if i - j == 0:
            self.lDiag += player
        if i + j == 2:
            self.rDiag += player
    
    def findResult(self):
        """
        0 - Draw
        1 - Player 1 won
        2 - Player 2 won
        3 - Game not yet finished
        """
        for i in range(3):
            if self.rowCnt[i] == 3 or self.colCnt[i] == 3:
                return 1
            if self.rowCnt[i] == -3 or self.colCnt[i] == -3:
                return 2
        if self.lDiag == 3 or self.rDiag == 3:
            return 1
        if self.lDiag == -3 or self.rDiag == -3:
            return 2
        if len(self.moves) == 9:
            return 0
        else:
            return 3