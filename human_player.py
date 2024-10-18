import pygame
import time

from game import Game

# ======================= Human player part =======================
class HumanPlayer():
    def __init__(self, game: Game) -> None:
        self.game = game
        self.last_time = time.time()
        self.wait_time = self.game.pygame_print.wait_time
    
    def play(self) -> None:
        while self.game.running:
            if time.time() - self.last_time > self.wait_time:
                # Event management
                events = pygame.event.get()
                
                if len(events) != 0:
                    event = events[0]
                    
                    if event.type == pygame.QUIT:
                        self.game.running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT: # Move to the right
                            self.game.new_event("RIGHT")
                            self.wait_time = self.game.pygame_print.wait_time
                        elif event.key == pygame.K_UP: # Jump
                            self.game.new_event("JUMP")
                            self.wait_time = self.game.pygame_print.wait_time * 2
                
                if self.game.running:
                    # Delete other events that are too fast
                    pygame.event.clear()

                self.last_time = time.time()
        
        # Victory or defeat condition
        if self.game.score == -100:
            print("You've fallen into a hole!")
        else:
            print(f"You've won with {self.game.score} points!")
