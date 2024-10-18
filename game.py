import random
from pygame_print import PygamePrint
import copy

# ======================= Game part ======================= 
class Game:
    def __init__(self, start_pos, grid, print_game=False, qtable=False, wait_time=0.03) -> None:
        self.start_pos = copy.deepcopy(start_pos)
        self.player_pos = copy.deepcopy(start_pos)
        self.original_grid = copy.deepcopy(grid)
        self.grid = copy.deepcopy(grid)
        self.print_game = print_game
        self.nb_diff = 0
        self.score = 0
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.running = True

        if (self.print_game):
            self.pygame_print = PygamePrint(game=self, qtable=qtable, wait_time=wait_time)
            self.pygame_print.draw_grid()
    
    def move_player(self, dx, dy) -> None:
        new_col = self.player_pos[0] + dx
        new_row = self.player_pos[1] + dy
        
        # Check the limits of the grid
        if 0 <= new_row < self.ROWS and 0 <= new_col < self.COLS:
            # Check whether the target cell is empty or the target cell is empty
            if self.grid[new_row][new_col] in {0, 5, 333}:
                self.player_pos[1], self.player_pos[0] = new_row, new_col
                self.nb_diff += 1

                if self.grid[new_row][new_col] == 5:
                    self.score += 5
                    self.grid[new_row][new_col] = 0
    
    def apply_gravity(self) -> None:
        if self.player_pos[1] < self.ROWS - 1 and self.grid[self.player_pos[1] + 1][self.player_pos[0]] in {0, 5}:
            self.player_pos[1] += 1

            self.apply_gravity()
    
    def new_event(self, move) -> None:
        in_jump = False

        if move == "RIGHT":
            self.move_player(1, 0)
            self.apply_gravity()
        elif move == "JUMP":
            in_jump = True      
            # Rising diagonal
            self.move_player(1, -1)
        
        if (self.print_game):
            self.pygame_print.draw_grid()
        
        if (in_jump):      
            # Downward diagonal
            self.move_player(1, 1)
            self.apply_gravity()

            if (self.print_game):
                self.pygame_print.draw_grid()
        
        # Victory or defeat condition
        if self.grid[self.player_pos[1]][self.player_pos[0]] == 333:
            print("Victory!")
            self.score += 100
            self.running = False

            if (self.print_game):
                self.pygame_print.quit()
        elif self.player_pos[1] == self.ROWS - 1 and self.grid[self.player_pos[1]][self.player_pos[0]] == 0:
            print("Defeat!")
            self.score = -100
            self.running = False

            if (self.print_game):
                self.pygame_print.quit()
    
    def get_state(self) -> int:
        return self.player_pos[0]
    
    def reset(self) -> None:
        self.player_pos = copy.deepcopy(self.start_pos)
        self.nb_diff = 0
        self.score = 0
        self.running = True
        self.grid = copy.deepcopy(self.original_grid)
        
        if (self.print_game):
            self.pygame_print.__init__(game=self, qtable=self.pygame_print.qtable, wait_time=self.pygame_print.wait_timee)
            self.pygame_print.draw_grid()
    
    def step(self, action) -> tuple:
        if action == 0:
            self.new_event("RIGHT")
        elif action == 1:
            self.new_event("JUMP")
        
        return self.get_reward(), not self.running
    
    def get_random_action(self) -> int:
        # Choose randomly between RIGHT and JUMP
        return random.randint(0, 1)
    
    # Return all valid moves
    def get_possible_moves(self) -> list:
        possible_moves = []

        if self.grid[self.player_pos[1]][self.player_pos[0] + 1] in {0, 5, 333}:  # Right is possible
            possible_moves.append("RIGHT")

        if self.player_pos[1] > 0 and self.grid[self.player_pos[1] - 1][self.player_pos[0]] in {0, 5, 333} and self.grid[self.player_pos[1] - 1][self.player_pos[0] + 1] in {0, 5, 333}:  # Jump is possible
            possible_moves.append("JUMP")

        return possible_moves
    
    # Return a deep copy of the game state for simulation
    def copy(self) -> object:
        return Game(copy.deepcopy(self.player_pos), copy.deepcopy(self.grid), False)

    # Reward system for win, loss, or intermediate steps
    def get_reward(self) -> float:
        if not self.running:
            return self.score + (self.player_pos[0] - self.start_pos[0]) / 100  # There's also a reward for getting around  # The score is already set on victory/loss
        
        return 0
