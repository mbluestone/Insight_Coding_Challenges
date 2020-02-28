import numpy as np

class MineSweeper():
    def __init__(self, board_size, num_mines):
        self.num_mines = num_mines
        self.board_size = board_size
        self.game_over = False
        
    def start_game(self):
        
        self.initialize_board()
        self.game_over = False

        while not self.game_over:
            print(self.visual_board)
            
            user_input = False
            while not user_input:
                response = input("Input X,Y coordinates of your move (e.g. 0 1):\n")
                user_input = self.process_user_input(response)
            
            x, y = user_input[0], user_input[1]
            
            if self.board[x,y] == -1:
                print(f'You hit a mine at {x} {y}! Game over!')
                print(self.board)
                self.game_over = True
                
            else:
                self.update_visual_board(x,y)

            if np.count_nonzero(self.visual_board=='-') == self.num_mines:
                print('Congrats you won!')
                self.game_over = True
            
    def update_visual_board(self,x,y):
        
        if self.board[x,y] != 0:
            self.visual_board[x,y] = self.board[x,y]
          
        # traverse board, check for non zeros, and fill in visual board
        else:
            
            def surrounding_cells(x,y):
                cells = []
                if x == 0:
                    check_x_range = range(x,x+2)
                elif x == self.board_size-1:
                    check_x_range = range(x-1,x+1)
                else:
                    check_x_range = range(x-1,x+2)

                if y == 0:
                    check_y_range = range(y,y+2)
                elif y == self.board_size-1:
                    check_y_range = range(y-1,y+1)
                else:
                    check_y_range = range(y-1,y+2)

                for x_check in check_x_range:
                    for y_check in check_y_range:
                        cells.append((x_check,y_check))
                        
                cells.remove((x,y))
                return cells
            
            def check_for_zeros(queue,already_checked):
                x,y = queue.pop(0)
                if self.board[x,y]!=0:
                    self.visual_board[x,y] = self.board[x,y]
                elif self.board[x,y]==0:
                    self.visual_board[x,y] = self.board[x,y]
                    new_inds = [inds for inds in surrounding_cells(x,y) 
                                if inds not in already_checked]
                    queue.extend(new_inds)
                already_checked.append((x,y))
                return queue
                    
            queue = surrounding_cells(x,y)
            already_checked = []
            while queue:
                queue = check_for_zeros(queue,already_checked)
                
            
            
    def process_user_input(self,response):
        try:
            xy = response.split()
            x = int(xy[0])
            y = int(xy[1])
            
            if x > self.board_size-1 or y > self.board_size-1:
                print(f"Incorrect input! You must input 2 numbers \
                    smaller than the board size\n")
                return False
            
            if self.visual_board[x,y]!= '-':
                print(f"You have already chosen this location, choose another\n")
                return False
            
            return x,y
        except:
            print(f"Incorrect input! You must input 2 numbers \
                    with a space between(e.g. 1 2), not {type(response)}\n")
            return False
        
    def initialize_board(self):
        
        self.board = np.zeros(self.board_size*self.board_size)
        
        mine_inds = np.random.choice(range(self.board_size*self.board_size), 
                                     self.num_mines, 
                                     replace=False)
        self.board[mine_inds] = -1
        
        self.board = self.board.reshape((self.board_size,self.board_size))
        
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.board[x,y] = self.check_for_mines(x,y)
        
        self.visual_board = np.empty((self.board_size,self.board_size),dtype=object)
        self.visual_board.fill('-')
            
    def check_for_mines(self,x,y):
        
        if self.board[x,y] == -1:
            return -1
        
        count = 0
        if x == 0:
            check_x_range = range(x,x+2)
        elif x == self.board_size-1:
            check_x_range = range(x-1,x+1)
        else:
            check_x_range = range(x-1,x+2)
            
        if y == 0:
            check_y_range = range(y,y+2)
        elif y == self.board_size-1:
            check_y_range = range(y-1,y+1)
        else:
            check_y_range = range(y-1,y+2)
        
        for check_x in check_x_range:
            for check_y in check_y_range:
                if self.board[check_x,check_y] == -1:
                    count += 1
                    
        return count
    