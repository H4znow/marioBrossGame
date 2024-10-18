from game import Game

# ======================= Bot player part (TEST) =======================
class BotPlayer():
    def __init__(self, game: Game) -> None:
        self.game = game
    
    def play(self) -> None:
        events = ["RIGHT", "RIGHT", "RIGHT", "JUMP", "JUMP", "JUMP", "RIGHT", "JUMP", "JUMP", "JUMP", "RIGHT", "JUMP", "RIGHT", "JUMP", "RIGHT", "JUMP", "RIGHT", "RIGHT", "RIGHT", "RIGHT", "JUMP", "JUMP", "RIGHT", "JUMP", "JUMP", "RIGHT", "RIGHT", "JUMP", "JUMP", "RIGHT", "JUMP", "RIGHT","RIGHT"]

        for event in events:
            self.game.new_event(event)
        
        # Victory or defeat condition
        if self.game.score == -100:
            print("You've fallen into a hole!")
        else:
            print(f"You've won with {self.game.score} points!")
