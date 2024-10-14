# ======================= Human player part (TODO) =======================
class HumanPlayer():
    def __init__(self, game) -> None:
        self.game = game
        self.play()
    
    def play(self) -> None:
        while self.game.running:
            user_input = int(input("Entrez un entier : "))
            self.game.new_event(user_input)