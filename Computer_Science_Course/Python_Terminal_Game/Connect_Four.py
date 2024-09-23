print("This is Connect Four Game")

class Connect_Four:
    player1_symbol = 'X'
    player2_symbol = 'O'

    def __init__(self):
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.is_player1 = True
    
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
                return
                
        if self.is_player1:
            self.board[row][column] = Connect_Four.player1_symbol
            self.is_player1 = False
        else:
            self.board[row][column] = Connect_Four.player2_symbol
            self.is_player1 = True

game = Connect_Four()
game.display_board()
game.player_play(0)
game.display_board()
game.player_play(0)
game.display_board()
