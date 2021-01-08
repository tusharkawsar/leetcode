class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, board, word, visited):
            # print(i, j, visited, word)
            # Base
            if len(word) == 0 or word is None:
                return True
            # Up
            if i-1 >= 0 and board[i-1][j] == word[0] and (i-1,j) not in visited:
                # print("UP")
                if dfs(i-1, j, board, word[1:], visited + [(i-1,j)]): return True 
            # Right
            if j+1 < len(board[0]) and board[i][j+1] == word[0] and (i,j+1) not in visited:
                # print("RIGHT")
                if dfs(i, j+1, board, word[1:], visited + [(i,j+1)]): return True 
            # Down
            if i+1 < len(board) and board[i+1][j] == word[0] and (i+1,j) not in visited:
                # print("DOWN")
                if dfs(i+1, j, board, word[1:], visited + [(i+1,j)]): return True 
            # Left
            if j-1 >= 0 and board[i][j-1] == word[0] and (i,j-1) not in visited:
                # print("LEFT")
                if dfs(i, j-1, board, word[1:], visited + [(i,j-1)]): return True 
                
            return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print("next iteration")
                if board[i][j] == word[0] and dfs(i, j, board, word[1:], visited=[(i,j)]): return True
                
        return False
            
            
