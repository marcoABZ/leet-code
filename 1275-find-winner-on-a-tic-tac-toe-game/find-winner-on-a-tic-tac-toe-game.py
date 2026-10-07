class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        rows = {0: [], 1: [], 2: []}
        cols = {0: [], 1: [], 2: []}
        diag = {0: [], 1: []}

        mov = 'X'
        for move in moves:
            rows[move[0]].append(mov)
            cols[move[1]].append(mov)
            if move[0] == move[1]:
                diag[0].append(mov)
            if (move[0] + move[1]) % 2 == 0 and (move[0] == 1 or move[0] != move[1]):
                diag[1].append(mov)
            
            mov = 'O' if mov == 'X' else 'X'
        
        for row in rows.values():
            if len(row) != 3:
                continue
            if all([x == 'X' for x in row]):
                return "A"
            if all([x == 'O' for x in row]):
                return "B"
        
        for col in cols.values():
            if len(col) != 3:
                continue
            if all([x == 'X' for x in col]):
                return "A"
            if all([x == 'O' for x in col]):
                return "B"
        
        for diag in diag.values():
            if len(diag) != 3:
                continue
            if all([x == 'X' for x in diag]):
                return "A"
            if all([x == 'O' for x in diag]):
                return "B"
        
        if len(moves) == 9:
            return "Draw"
        return "Pending"
        
