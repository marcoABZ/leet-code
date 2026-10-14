class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, curr, i, j, visited=set()):
            if curr == word:
                return True

            for pos in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[0]):
                    continue
                if pos in visited:
                    continue

                if board[pos[0]][pos[1]] == word[len(curr)]:
                    visited.add(pos)
                    if dfs(board, word, curr + board[pos[0]][pos[1]], pos[0], pos[1], visited):
                        return True
                    visited.remove(pos)

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, word, word[0], i, j, set([(i, j)])):
                        return True
        
        return False
        