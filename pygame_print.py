import pygame
import time
import numpy as np

# ======================= Print game part ======================= 
class PygamePrint():
    def __init__(self, game, qtable=False, wait_time=0.03) -> None:
        self.game = game
        self.WIDTH, self.HEIGHT = 600, 300
        self.CELL_SIZE = 50
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FILLED_FINISH_COLOR = (255, 0, 0)
        self.FILLED_DEFAULT_COLOR = (0, 255, 0)
        self.FILLED_PIECE_COLOR = (255, 255, 0)
        self.FILLED_PLAYER_COLOR = (0, 0, 255)
        self.wait_time = wait_time
        self.qtable = qtable

        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Mario Bros")
    
    def draw_arrow(self, direction, x, y) -> None:
        center = (x + self.CELL_SIZE // 3, y + self.CELL_SIZE // 2)
        
        if direction[0] < direction[1]: # Jump
            pygame.draw.line(self.window, self.BLACK, (center[0] + 8, center[1] + 8), (center[0] + 8, center[1] - 7), 3)
            pygame.draw.polygon(self.window, self.BLACK, [(center[0] + 8, center[1] - 12), (center[0] + 3, center[1] - 2), (center[0] + 13, center[1] - 2)])
        else: # Right
            pygame.draw.line(self.window, self.BLACK, center, (center[0] + 15, center[1]), 3)
            pygame.draw.polygon(self.window, self.BLACK, [(center[0] + 20, center[1]), (center[0] + 10, center[1] - 5), (center[0] + 10, center[1] + 5)])
    
    # Function for drawing the grid and the player
    def draw_grid(self) -> None:
        self.window.fill(self.WHITE)  # Fill the background with white
        
        if self.qtable:
            qtable = np.load("q_table.npy")

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
                
                if self.qtable and row + 1 < self.game.ROWS and self.game.grid[row + 1][col] == 1 and self.game.grid[row][col] in {0, 5, 333}:
                    self.draw_arrow(qtable[col], x, y)

        # Draw the player
        player_x = self.game.start_pos[0] * self.CELL_SIZE 
        player_y = self.game.player_pos[1] * self.CELL_SIZE
        pygame.draw.rect(self.window, self.FILLED_PLAYER_COLOR, (player_x, player_y, self.CELL_SIZE, self.CELL_SIZE))
        
        if self.qtable and self.game.grid[self.game.player_pos[1] - 1][self.game.player_pos[0]] in {0, 5, 333}:
            self.draw_arrow(qtable[self.game.player_pos[0]], player_x, player_y)

        pygame.display.update()  # Update the display
        time.sleep(self.wait_time)
    
    def quit(self) -> None:
        pygame.quit()
