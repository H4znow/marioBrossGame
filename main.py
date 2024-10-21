import time

from game import Game
from human_player import HumanPlayer
from bot_player import BotPlayer
from mcts_player import MCTSPlayer
from q_learning_player import QLearningPlayer
from q_table_player import QTablePlayer

# ======================= Main part =======================

# Example map (0 = empty, 1 = full, 5 coin, 333 = arrival)
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 333, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 333, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 333, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 333, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Initial player position
player_pos = [5, 3]

def choose_player():
    user_input = input(
        "Choose a player :\n"
        "1) Human player\n"
        "2) Bot player\n"
        "3) MCTS player\n"
        "4) Learning player for Q-table\n"
        "5) Q-table player\n"
        "Your choice : "
    )
    
    def print_q_table():
        user_input = input(
            "Display the Q-table to see the difference ?\n"
            "0) no\n"
            "1) yes\n"
            "Your choice : "
        )
        
        options = {
            "0": False,
            "1": True,
        }
        
        if user_input in options:
            return options[user_input]
        
        print("Invalid choice. Please try again.")
        print_q_table()

    def human_player():
        game = Game(start_pos=player_pos, grid=grid, print_game=True, qtable=print_q_table(), wait_time=0.1)
        human = HumanPlayer(game)
        time.sleep(1)
        human.play()

    def bot_player():
        game = Game(start_pos=player_pos, grid=grid, print_game=True, qtable=print_q_table(), wait_time=0.1)
        bot = BotPlayer(game)
        time.sleep(1)
        bot.play()

    def mcts_player():
        game = Game(start_pos=player_pos, grid=grid, print_game=True, qtable=print_q_table(), wait_time=0.1)
        mcts = MCTSPlayer(game)
        time.sleep(1)
        mcts.play()
    
    def print_game():
        user_input = input(
            "Do you want to view live progress (this is slower) ?\n"
            "0) no\n"
            "1) yes\n"
            "Your choice : "
        )
        
        options = {
            "0": False,
            "1": True,
        }
        
        if user_input in options:
            return options[user_input]
        
        print("Invalid choice. Please try again.")
        print_game()

    def learning_q_table():
        game = Game(start_pos=player_pos, grid=grid, print_game=print_game(), qtable=True, wait_time=0.03)
        q_learning = QLearningPlayer(game)
        q_learning.train(1000)

    def q_table_player():
        game = Game(start_pos=player_pos, grid=grid, print_game=True, qtable=True, wait_time=0.1)
        q_table = QTablePlayer(game)
        time.sleep(1)
        q_table.play()

    options = {
        "1": human_player,
        "2": bot_player,
        "3": mcts_player,
        "4": learning_q_table,
        "5": q_table_player,
    }

    if user_input in options:
        options[user_input]()
    else:
        print("Invalid choice. Please try again.")
        choose_player()

choose_player()
