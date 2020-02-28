import numpy as np
class ConnectFour():
    def __init__(self):
        self.board = np.zeros((4,4))
        self.visual_board = np.empty((4,4),dtype=object)
        self.visual_board.fill('-')
        self.player_dict = {1: '1', -1: '2'}
        self.full_board = False
        
    def start_game(self):
        
        self.game_over = False
        self.current_player = 1
        
        while not self.full_board:
        
            print(self.visual_board)
            valid_move = False
            while not valid_move:
                
                valid_move = self.user_input()
                
            self.check_game_over()

            self.current_player *= -1
            
        print('Tie game!')
        print(self.visual_board)
        
        
    def user_input(self):
        
        response = input(f"Player {self.player_dict[self.current_player]} make your move.")
        
        response = int(response)
        
        #"Illegal move"
        
        #"This column is full.  Try another one!", 
        
        
        #"The board is full!"
        
        for i,row in enumerate(self.board[::-1]):
            if row[response] == 0:
                row[response] = self.current_player
                self.visual_board[len(self.board)-1-i][response] = self.player_dict[self.current_player]
                return True
            
        
    def check_game_over(self):
        
        # check columns
        if any(abs(sum(self.board))==4):
            self.game_over = True
            print(f"Player {self.player_dict[self.current_player]} wins!")
        
        # check rows
        elif any([abs(sum(row))==4 for row in board]):
            self.game_over = True
            print(f"Player {self.player_dict[self.current_player]} wins!")
            
        # check diagonals
        elif abs(sum([self.board[i][i] for i in range(len(self.board))]))==4:
            self.game_over = True
            print(f"Player {self.player_dict[self.current_player]} wins!")
            
        elif abs(sum([self.board[i][len(self.board)-1-i] for i in range(len(self.board))]))==4:
            self.game_over = True
            print(f"Player {self.player_dict[self.current_player]} wins!")
           
        # check if full board
        elif not any([any(i==0) for i in board]):
            self.full_board = True
            
        