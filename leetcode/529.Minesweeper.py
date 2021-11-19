class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click[0], click[1]
        char = board[row][col]

        # If a mine is clicked then return immediately
        if char == 'M':
            board[row][col] = 'X'
            return board
        
        # otherwise recursizely reveal squares until you find a square that has adjacent mines
        self.revealSquares(board, row, col)
        return board
            
    def revealSquares(self, board, row, col):
        # if we hit a mine or a square with adjacent mines return
        if board[row][col] != 'E':
            return
        
        # store all possible directions so that we can easily loop through them
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        
        # determine if there are any mines adjacent to the current square
        num_adj = 0
        for direct in directions:
            new_row = row + direct[0]
            new_col = col + direct[1]
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'M':
                num_adj += 1
        
        # if there are any adjacent mines then set the square to be the number of adjacent mines and return
        if num_adj > 0:
            board[row][col] = str(num_adj)
            return
        
        # otherwise set the square to be blank and recursively reveal all adjacent squares
        board[row][col] = 'B'
        
        for direct in directions:
            new_row = row + direct[0]
            new_col = col + direct[1]
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                self.revealSquares(board, new_row, new_col)
        