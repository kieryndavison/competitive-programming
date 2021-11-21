class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Set first bit to be the new value and the second bit to be the old value 
        for i in range(len(board)):
            for j in range(len(board[0])):
                directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
                
                live_cells = 0
                for direct in directions:
                    new_i = i + direct[0]
                    new_j = j + direct[1]
                    
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                        live_cells += board[new_i][new_j] & 1
                        
                if board[i][j] == 0 and live_cells == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and 2 <= live_cells <= 3:
                    board[i][j] = 3
        
        # Converts the values in the board to be the new value using a bitwise right shift
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
                