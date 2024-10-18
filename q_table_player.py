import numpy as np

from game import Game

# ======================= Qtable player part (TEST) =======================
class QTablePlayer():
    def __init__(self, game: Game) -> None:
        self.game = game
    
    def play(self) -> None:
        qtable = np.load("q_table.npy")
        
        while self.game.running:
            event = qtable[self.game.player_pos[1]]
            
            new_event = "JUMP" if event[0] < event[1] else "RIGHT"
            self.game.new_event(new_event)
        
        # Victory or defeat condition
        if self.game.score == -100:
            print("You've fallen into a hole!")
        else:
            print(f"You've won with {self.game.score} points!")
