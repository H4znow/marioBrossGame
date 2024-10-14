# ======================= Bot player part (TEST) =======================
class BotPlayer():
    def __init__(self, game) -> None:
        self.game = game
        self.play()
    
    def play(self) -> None:
        events = ["RIGHT", "RIGHT", "RIGHT", "JUMP", "JUMP", "JUMP", "RIGHT", "JUMP", "JUMP", "JUMP", "RIGHT", "JUMP", "RIGHT", "JUMP", "RIGHT", "JUMP", "RIGHT", "RIGHT", "RIGHT", "RIGHT", "JUMP", "JUMP", "RIGHT", "JUMP", "JUMP", "RIGHT", "RIGHT", "JUMP", "JUMP", "RIGHT", "JUMP", "RIGHT","RIGHT"]

        for event in events:
            self.game.new_event(event)