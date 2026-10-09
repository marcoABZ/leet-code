class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ri, rj = None, None
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    ri = i
                    rj = j
                    break
            if ri is not None:
                break
        
        result = 0
        for i in range(ri-1,-1,-1):
            if board[i][rj] == ".":
                continue
            if board[i][rj] == 'B':
                break
            else:
                result += 1
                break
        
        for i in range(ri+1,8):
            if board[i][rj] == ".":
                continue
            if board[i][rj] == "B":
                break
            else:
                result += 1
                break
        
        for j in range(rj-1,-1,-1):
            if board[ri][j] == ".":
                continue
            if board[ri][j] == "B":
                break
            else:
                result += 1
                break
        
        for j in range(rj,8):
            if board[ri][j] == "B":
                break
            elif board[ri][j] == "p":
                result += 1
                break
        
        return result