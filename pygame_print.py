import pygame
import time

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
                
                if self.game.grid[row][col] == 1:
                    color = self.FILLED_DEFAULT_COLOR
                if self.game.grid[row][col] == 5:
                    color = self.FILLED_PIECE_COLOR
                elif self.game.grid[row][col] == 333:
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