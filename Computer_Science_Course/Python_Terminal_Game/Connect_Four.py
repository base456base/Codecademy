class Connect_Four:
    player1_symbol = 'X'
    player2_symbol = 'O'

    def __init__(self):
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.is_player1 = True
        self.is_draw = False

    def display_board(self):
        text_length = 0
        for column in self.board:
            row_text = "| "
            for row in column:
                if row is None:
                    row_text += "  | "
                else:
                    row_text += f"{row}" + " | "
            
            print(row_text)
            text_length = len(row_text)
        print("-" * text_length)
                
    def player_play(self, column):
        row = 5
        while (self.board[row][column] != None):
            row -= 1
            if row < 0:
                print("This column is full, please play other column.")
                return False
    
        
        if self.is_player1:
            self.board[row][column] = Connect_Four.player1_symbol
            self.is_player1 = False
            if self.check_draw():
                return self.is_draw
            return self.check_win(Connect_Four.player1_symbol) 
        else:
            self.board[row][column] = Connect_Four.player2_symbol
            self.is_player1 = True
            if self.check_draw():
                return self.is_draw
            return self.check_win(Connect_Four.player2_symbol)

    def check_draw(self):
        count_last_row = 0
        column_last_row = 0
        while (column_last_row < 7):
            if self.board[0][column_last_row] != None:
                count_last_row += 1
            column_last_row += 1
        if count_last_row >= 7:
            self.is_draw = True
            return True
   

    def check_win(self, player_symbol):
        # Get dimensions of the board
        rows = len(self.board)
        cols = len(self.board[0])
        
        # Check horizontal wins
        for row in range(rows):
            for col in range(cols - 3):  # Only go up to the 4th last column
                if self.board[row][col] == player_symbol and self.board[row][col+1] == player_symbol and \
                self.board[row][col+2] == player_symbol and self.board[row][col+3] == player_symbol:
                    return True
        
        # Check vertical wins
        for row in range(rows - 3):  # Only go up to the 4th last row
            for col in range(cols):
                if self.board[row][col] == player_symbol and self.board[row+1][col] == player_symbol and \
                self.board[row+2][col] == player_symbol and self.board[row+3][col] == player_symbol:
                    return True
        
        # Check diagonal wins (top-left to bottom-right)
        for row in range(rows - 3):
            for col in range(cols - 3):
                if self.board[row][col] == player_symbol and self.board[row+1][col+1] == player_symbol and \
                self.board[row+2][col+2] == player_symbol and self.board[row+3][col+3] == player_symbol:
                    return True
        
        # Check diagonal wins (top-right to bottom-left)
        for row in range(rows - 3):
            for col in range(3, cols):
                if self.board[row][col] == player_symbol and self.board[row+1][col-1] == player_symbol and \
                self.board[row+2][col-2] == player_symbol and self.board[row+3][col-3] == player_symbol:
                    return True
        
        # If no win is found, return False
        return False

game = Connect_Four()
print("The game is start!")
while True:
    if game.is_player1:
        print("Player 1 's Turn")
    else:
        print("Player 2 's Turn")
    game.display_board()
    played_column = input("Please enter the column (0-6): ")
    if played_column not in ['0', '1', '2', '3', '4', '5', '6']:
        continue
    is_done = game.player_play(int(played_column))

    if is_done:
        game.display_board()
        if game.is_draw:
            print("Draw !")
            break
        if not game.is_player1:
            print("Player 1 Win !")
        else:
            print("Player 2 Win !")
        break
