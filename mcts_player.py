import math
import random

# ======================= MCTS player part =======================
class MCTSPlayer:
    def __init__(self, game, iterations=20, exploration_weight=1.4):
        self.game = game
        self.iterations = iterations  # Number of iterations for MCTS
        self.exploration_weight = exploration_weight  # Exploration/exploitation balance weight
        self.Q = {}  # Total reward of each state
        self.N = {}  # Number of visits to each state
        self.children = {}  # List of possible moves for each state
        
        # Main game play
        self.play()

    def choose(self):
        # Perform MCTS to select the best move
        for _ in range(self.iterations):
            self.run_simulation()

        # Find the most visited node to choose the best move
        state = self.serialize(self.game)
        
        if state not in self.children:
            return random.choice(self.game.get_possible_moves())  # Fallback to a random move if no children exist

        # Choose the action that has been visited the most
        possible_moves = self.children[state]
        best_move = max(possible_moves, key=lambda move: self.N.get((state, move), 0))
        
        return best_move

    def run_simulation(self):
        # Start from a copy of the current game state
        simulation_game = self.game.copy()
        path = []
        
        # Selection and expansion phase
        while True:
            state = self.serialize(simulation_game)
            
            if state not in self.children:  # Expand the node
                self.children[state] = simulation_game.get_possible_moves()
                break
            
            # If all moves have been tried, select the best move using UCT
            if not self.children[state]:  # If no moves available, the game ends
                return 0  # No reward if no moves can be made

            # Select the best move using UCT
            move = self.select_move(state)
            path.append((state, move))
            simulation_game.new_event(move)

            # Stop the simulation if the game is over
            if not simulation_game.running:
                break

        # Simulation phase: simulate until the game ends
        reward = self.simulate_to_end(simulation_game)

        # Backpropagation phase: propagate the reward back up the tree
        for state, move in path:
            if (state, move) in self.N:
                self.N[(state, move)] += 1
                self.Q[(state, move)] += reward
            else:
                self.N[(state, move)] = 1
                self.Q[(state, move)] = reward

    def select_move(self, state):
        # Upper Confidence Bound for Trees (UCT)
        total_visits = sum(self.N.get((state, move), 0) for move in self.children[state])
        log_total_visits = math.log(total_visits + 1)

        def uct(move):
            # Exploitation value (average reward) + exploration value
            q_value = self.Q.get((state, move), 0)
            visit_count = self.N.get((state, move), 0)
            
            if visit_count == 0:
                return float("inf")  # Prioritize unvisited moves
            
            return q_value / visit_count + self.exploration_weight * math.sqrt(log_total_visits / visit_count)

        # Return the move with the highest UCT value
        return max(self.children[state], key=uct)

    def simulate_to_end(self, game):
        # Simulate random moves until the game ends and return the final reward
        while game.running:
            possible_moves = game.get_possible_moves()
            
            if not possible_moves:
                break
            
            random_move = random.choice(possible_moves)
            game.new_event(random_move)

        return game.get_reward()

    def serialize(self, game):
        # Serialize the game state as a string (player position + grid)
        return (tuple(game.player_pos), tuple(tuple(row) for row in game.grid))
    
    def play(self):
        # Keep playing while the game is still running
        while self.game.running:
            # Run MCTS to determine the next move
            move = self.choose()
            # Apply the selected move in the game
            self.game.new_event(move)
        
        # Victory or defeat condition
        if self.game.score == -100:
            print("You've fallen into a hole!")
        else:
            print(f"You've won with {self.game.score} points!")
