from pygame_print import PygamePrint
import copy

# ======================= Game part ======================= 
class Game:
    def __init__(self, start_pos, grid, print_game) -> None:
        self.start_pos = copy.deepcopy(start_pos)
        self.player_pos = start_pos
        self.grid = grid
        self.print_game = print_game
        self.nb_diff = 0
        self.score = 0
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.running = True

        if (self.print_game):
            self.pygame_print = PygamePrint(self)
            self.pygame_print.draw_grid()
    
    def move_player(self, dx, dy) -> None:
        new_row = self.player_pos[0] + dy
        new_col = self.player_pos[1] + dx
        
        # Check the limits of the grid
        if 0 <= new_row < self.ROWS and 0 <= new_col < self.COLS:
            # Check whether the target cell is empty or the target cell is empty
            if self.grid[new_row][new_col] in {0, 5, 333}:
                self.player_pos[0], self.player_pos[1] = new_row, new_col
                self.nb_diff += 1

                if self.grid[new_row][new_col] == 5:
                    self.score += 5
                    self.grid[new_row][new_col] = 0
    
    def apply_gravity(self) -> None:
        if self.player_pos[0] < self.ROWS - 1 and self.grid[self.player_pos[0] + 1][self.player_pos[1]] in {0, 5}:
            self.player_pos[0] += 1

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
        if self.grid[self.player_pos[0]][self.player_pos[1]] == 333:
            self.score += 100
            self.running = False

            if (self.print_game):
                self.pygame_print.quit()
        elif self.player_pos[0] == self.ROWS - 1 and self.grid[self.player_pos[0]][self.player_pos[1]] == 0:
            self.score = -100
            self.running = False

            if (self.print_game):
                self.pygame_print.quit()
    
    # Return all valid moves
    def get_possible_moves(self):
        possible_moves = []

        if self.grid[self.player_pos[0]][self.player_pos[1] + 1] in {0, 5, 333}:  # Right is possible
            possible_moves.append("RIGHT")

        if self.player_pos[0] > 0 and self.grid[self.player_pos[0] - 1][self.player_pos[1]] in {0, 5, 333} and self.grid[self.player_pos[0] - 1][self.player_pos[1] + 1] in {0, 5, 333}:  # Jump is possible
            possible_moves.append("JUMP")

        return possible_moves
    
    # Return a deep copy of the game state for simulation
    def copy(self):
        return Game(copy.deepcopy(self.player_pos), copy.deepcopy(self.grid), False)

    # Reward system for win, loss, or intermediate steps
    def get_reward(self):
        if not self.running:
            return self.score  # The score is already set on victory/loss
        
        return 0
