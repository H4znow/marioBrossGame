import time
import pygame
import copy

# ======================= Print game part ======================= 
class PygamePrint():
    def __init__(self, game) -> None:
        self.game = game
        self.WIDTH, self.HEIGHT = 600, 300
        self.CELL_SIZE = 50
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FILLED_FINISH_COLOR = (255, 0, 0)
        self.FILLED_DEFAULT_COLOR = (0, 255, 0)
        self.FILLED_PIECE_COLOR = (255, 255, 0)
        self.FILLED_PLAYER_COLOR = (0, 0, 255)
        self.WAIT_TIME = 0.2

        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Mario Bros")

    
    # Function for drawing the grid and the player
    def draw_grid(self) -> None:
        self.window.fill(self.WHITE)  # Fill the background with white

        for row in range(self.game.ROWS):
            for col in range(self.game.COLS):
                # Position x, y of the top left corner of the cell
                x = (col * self.CELL_SIZE) - (self.game.nb_diff * self.CELL_SIZE)
                y = row * self.CELL_SIZE

                # Draw filled cells
                color = self.WHITE  # default colour
                
                if grid[row][col] == 1:
                    color = self.FILLED_DEFAULT_COLOR
                if grid[row][col] == 5:
                    color = self.FILLED_PIECE_COLOR
                elif grid[row][col] == 333:
                    color = self.FILLED_FINISH_COLOR

                pygame.draw.rect(self.window, color, (x, y, self.CELL_SIZE, self.CELL_SIZE))
                # Draw the outline of each cell
                pygame.draw.rect(self.window, self.BLACK, (x, y, self.CELL_SIZE, self.CELL_SIZE), 1)

        # Draw the player
        player_x = self.game.start_pos[1] * self.CELL_SIZE 
        player_y = self.game.player_pos[0] * self.CELL_SIZE
        pygame.draw.rect(self.window, self.FILLED_PLAYER_COLOR, (player_x, player_y, self.CELL_SIZE, self.CELL_SIZE))

        pygame.display.update()  # Update the display
        time.sleep(self.WAIT_TIME)

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
        self.in_jump = False
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
        if self.player_pos[0] < self.ROWS - 1 and self.grid[self.player_pos[0] + 1][self.player_pos[1]] == 0:
            self.player_pos[0] += 1

            self.apply_gravity()
    
    def new_event(self, move) -> None:
        if (self.in_jump):      
            # Downward diagonal
            self.move_player(1, 1)
            self.in_jump = False
            self.apply_gravity()

            if (self.print_game):
                self.pygame_print.draw_grid()
        
        if move == "RIGHT":
            self.move_player(1, 0)
            self.apply_gravity()
        elif move == "JUMP":
            self.in_jump = True      
            # Rising diagonal
            self.move_player(1, -1)
        
        if (self.print_game):
            self.pygame_print.draw_grid()
        
        # Victory or defeat condition
        if self.grid[self.player_pos[0]][self.player_pos[1]] == 333:
            self.score += 100
            self.running = False
        elif self.player_pos[0] == self.ROWS - 1 and self.grid[self.player_pos[0]][self.player_pos[1]] == 0:
            self.score = -100
            self.running = False

# ======================= Human player part (TODO) =======================
class HumanPlayer():
    def __init__(self, game) -> None:
        self.game = game
        self.play()
    
    def play(self) -> None:
        while self.game.running:
            user_input = int(input("Entrez un entier : "))
            self.game.new_event(user_input)

# ======================= Bot player part (TEST)=======================
class BotPlayer():
    def __init__(self, game) -> None:
        self.game = game
        self.play()
    
    def play(self) -> None:
        events = ["RIGHT", "RIGHT", "RIGHT", "JUMP", "JUMP", "JUMP", "RIGHT", "JUMP", "JUMP", "JUMP", "RIGHT", "JUMP", "RIGHT", "JUMP", "RIGHT", "JUMP", "RIGHT", "RIGHT", "RIGHT", "RIGHT", "JUMP", "JUMP", "RIGHT", "JUMP", "JUMP", "RIGHT", "RIGHT", "JUMP", "JUMP", "RIGHT", "JUMP", "RIGHT","RIGHT"]

        for event in events:
            self.game.new_event(event)


# ======================= Main part =======================

# Example map (0 = empty, 1 = full, 5 coin, 333 = arrival)
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Initial player position
player_pos = [3, 5]

game = Game(player_pos, grid, True)

player = BotPlayer(game)
