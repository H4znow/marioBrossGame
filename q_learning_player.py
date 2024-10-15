import numpy as np
import random
from game import Game

class QLearningPlayer:
    def __init__(self, game: Game, learning_rate=0.1, discount_factor=0.99, exploration_rate=1.0, exploration_decay=0.995):
        self.game = game
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.nb_actions = 2
        self.nb_states = 45
        self.penalty = -0.1
        self.q_table = np.zeros((self.nb_states,self.nb_actions))
        self.state = self.get_state()

    def get_state(self):
        return self.game.get_state()

    def choose_action(self):
        if random.uniform(0, 1) < self.exploration_rate:
            return self.game.get_random_action()
        else:
            state = self.get_state()
            if state not in self.q_table:
                return self.game.get_random_action()
            return np.argmax(self.q_table[state])

    def update_q_table(self, action, reward, next_state, penalty=2):
        state = self.get_state()
        max_future_q = np.max(self.q_table[next_state])
        current_q = self.q_table[state][action]

        # Apply penalty to the reward
        adjusted_reward = reward - penalty

        # Q-learning formula with penalty
        self.q_table[state][action] = current_q + self.learning_rate * (adjusted_reward + self.discount_factor * max_future_q - current_q)
      
    def play_step(self):
        action = self.choose_action()
        reward, done = self.game.step(action)
        next_state = self.get_state()
        self.update_q_table(action, reward, next_state)
        self.state = next_state
        return done        
            

    def train(self, episodes):
        for episode in range(episodes):
            self.game.reset()
            print(f"Episode {episode}")
            self.state = self.get_state()
            done = False
            while not done:
                self.exploration_rate *= self.exploration_decay
                done = self.play_step()
        print(self.q_table)
            