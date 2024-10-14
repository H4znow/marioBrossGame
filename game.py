import time
import pygame

# Window dimensions
WIDTH, HEIGHT = 600, 300
# Grid dimensions
ROWS, COLS = 6, 75
# Size of each cell
CELL_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FILLED_FINISH_COLOR = (255, 0, 0)
FILLED_DEFAULT_COLOR = (0, 255, 0)
FILLED_PIECE_COLOR = (255, 255, 0)
FILLED_PLAYER_COLOR = (0, 0, 255)

# Example map (0 = empty, 1 = full, 5 rooms, 333 = arrival)
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

# Pygame initiator
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Bros")

# Game variables
nb_diff = 0
score = 0
in_jump = False
running = True
print_pygame = False
last_time = time.time()

# ======================= Game part ======================= 

# Function to move the player
def move_player(dx, dy):
    global nb_diff, score
    
    new_row = player_pos[0] + dy
    new_col = player_pos[1] + dx
    
    # Check the limits of the grid
    if 0 <= new_row < ROWS and 0 <= new_col < COLS:
        # Check whether the target cell is empty or the target cell is empty
        if grid[new_row][new_col] in {0, 5, 333}:
            player_pos[0], player_pos[1] = new_row, new_col
            nb_diff += 1
            
            if grid[new_row][new_col] == 5:
                score += 5
                grid[new_row][new_col] = 0

# Function to apply gravity (if the player doesn't have a brick underneath, he falls)
def apply_gravity():
    if player_pos[0] < ROWS - 1 and grid[player_pos[0] + 1][player_pos[1]] == 0:
        player_pos[0] += 1

        apply_gravity()

# 38 up, 39 right
def new_event(code):
    global in_jump, score

    if (in_jump):      
        # Downward diagonal
        move_player(1, 1)
        in_jump = False
        apply_gravity()
    else:
        if code == 39: # Move to the right
            move_player(1, 0)
            apply_gravity()
        elif code == 38: # Jump
            in_jump = True      
            # Rising diagonal
            move_player(1, -1)

    # Victory or defeat condition
    if grid[player_pos[0]][player_pos[1]] == 333:
        score += 100

        return (False, score)
    
    if player_pos[0] == ROWS - 1 and grid[player_pos[0]][player_pos[1]] == 0:
        score = -100

        return (False, score)
    
    return (True, score)

# ======================= Pygame part ======================= 

# Function for drawing the grid and the player
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            # Position x, y of the top left corner of the cell
            x = (col * CELL_SIZE) - (nb_diff * CELL_SIZE)
            y = row * CELL_SIZE

            # Draw filled cells
            color = WHITE  # default colour
            
            if grid[row][col] == 1:
                color = FILLED_DEFAULT_COLOR
            if grid[row][col] == 5:
                color = FILLED_PIECE_COLOR
            elif grid[row][col] == 333:
                color = FILLED_FINISH_COLOR

            pygame.draw.rect(window, color, (x, y, CELL_SIZE, CELL_SIZE))
            # Draw the outline of each cell
            pygame.draw.rect(window, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

    # Draw the player
    player_x = 5 * CELL_SIZE # 5: player's initial position
    player_y = player_pos[0] * CELL_SIZE
    pygame.draw.rect(window, FILLED_PLAYER_COLOR, (player_x, player_y, CELL_SIZE, CELL_SIZE))

# Main loop
while running:
    window.fill(WHITE)  # Fill the background with white
    draw_grid()         # Draw the grid and the player
    pygame.display.update()
    
    if (in_jump):
        running, _ = new_event(0)

        last_time = time.time()
    elif (time.time() - last_time > 0.2):
        last_time = time.time()
        # Event management
        events = pygame.event.get()
        
        if len(events) != 0:
            event = events[0]
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: # Move to the right
                    running, _ = new_event(39)
                elif event.key == pygame.K_UP: # Jump
                    player_pos_before = [player_pos[0], player_pos[1]]

                    running, _ = new_event(38)

                    if player_pos[0] != player_pos_before[0] or player_pos[1] != player_pos_before[1]:
                        pygame.time.wait(200)
        
        # Delete other events that are too fast
        pygame.event.clear()

# Victory or defeat condition
if score == -100:
    print("You've fallen into a hole!")
else:
    print(f"You've won with {score} points!")

# Quit Pygame
pygame.quit()
