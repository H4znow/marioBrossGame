import numpy as np
import random

from game import Game

class QLearningPlayer:
    def __init__(self, game: Game, learning_rate=0.1, discount_factor=0.99, exploration_rate=1.0, load_qtable=False):
        self.game = game
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = 0.001
        self.nb_actions = 2
        self.nb_states = self.game.COLS
        self.penalty = -0.1
        self.q_table = np.zeros((self.nb_states,self.nb_actions))
        
        if load_qtable:
            self.q_table = np.load("q_table.npy")
            
        self.state = self.get_state()

    def get_state(self) -> int:
        return self.game.get_state()

    def choose_action(self):
        if random.uniform(0, 1) < self.exploration_rate:
            return self.game.get_random_action()
        
        state = self.state
        
        return np.argmax(self.q_table[state])

    def update_q_table(self, action, reward, next_state, penalty=1) -> None:
        state = self.state
        max_future_q = np.max(self.q_table[next_state])
        current_q = self.q_table[state][action]

        # Apply penalty to the reward
        adjusted_reward = reward - penalty

        # Q-learning formula with penalty
        self.q_table[state][action] = (1 - self.learning_rate) * current_q + self.learning_rate * (adjusted_reward + self.discount_factor * max_future_q)
    
    def play_step(self) -> bool:
        action = self.choose_action()
        reward, done = self.game.step(action)
        
        if done :
            print("reward: ", reward)
            
        next_state = self.get_state()
        self.update_q_table(action, reward, next_state)
        self.state = next_state
        
        return done        
            

    def train(self, episodes) -> None:
        self.exploration_decay = 1 / episodes
        
        for episode in range(episodes):
            self.game.reset()
            self.exploration_rate = (episodes - episode) * self.exploration_decay
            print(f"Episode {episode}")
            self.state = self.game.start_pos[1]
            done = False
            
            while not done:
                
                done = self.play_step()
            self.save_q_table("q_table.npy")
            
        print(self.q_table)

    def save_q_table(self, filename) -> None:
        np.save(filename, self.q_table)
            